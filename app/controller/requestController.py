from flask import Blueprint, request, render_template, redirect, url_for, flash, abort, jsonify
from flask_login import login_required, current_user

from app.models.assignQ import AssignQ
from app.models.base import db
from app.models.course import Course, CourseCategory
from app.models.experiment import Experiment, ExperimentStatus
from app.models.helpTopic import Helptopic
from app.models.llmanswer import LLMAnswer
from app.models.llmscore import LLMScore
from app.models.questionVariation import QuestionVariation
from app.models.request import Request, RequestType, Status

requestBP = Blueprint('request', __name__, url_prefix='/requests')


def is_teacher():
    return current_user.is_authenticated and current_user.utype == 'Teacher'


def is_admin():
    return current_user.is_authenticated and current_user.utype == 'Admin'

def is_student():
    return current_user.is_authenticated and current_user.utype == 'Student'


@requestBP.route('/', methods=['GET'])
@login_required
def view_requests():
    request_types = list(RequestType)

    if is_teacher():
        # Fetch all requests made by the current user
        request_types = [request_types[0],request_types[1],request_types[2], request_types[3]]
        user_requests = Request.query.filter_by(user_id=current_user.id).all()
        return render_template('teacher_requests.html', requests=user_requests, request_types=request_types)

    if is_admin():
        all_requests = Request.query.all()
        return render_template('request_list.html', requests=all_requests, request_types=request_types)


    if is_student():
        # Fetch all requests made by the current user
        user_requests = Request.query.filter_by(user_id=current_user.id).all()
        request_types = [request_types[3], request_types[4]]
        return render_template('student_requests.html', requests=user_requests, request_types=request_types)


    abort(403)


@requestBP.route('/handle/<int:request_id>', methods=['GET', 'POST'])
@login_required
def handle_requests(request_id):
    if not is_admin():
        abort(403)

    curr_request = Request.query.get_or_404(request_id)
    if request.method == 'POST':
        decision = request.form.get('decision')

        if not decision:
            flash('Missing inputs.', 'error')
            return redirect(url_for('request.handle_requests', request_id=request_id))

        if decision == 'pass':
            if curr_request.request_type == RequestType.ADD_COURSE:

                new_course = Course(curr_request.col1, int(curr_request.col2), curr_request.col3)
                db.session.add(new_course)
                db.session.commit()
                curr_request.status = Status.PASSED
                db.session.commit()
                flash('New course added to the database!', 'success')
                return redirect(url_for('request.view_requests'))

            if curr_request.request_type == RequestType.ADD_QUESTION:
                new_question = AssignQ(curr_request.col1, curr_request.col2, curr_request.col3)
                db.session.add(new_question)
                db.session.commit()
                # add a default variation
                last_question = db.session.query(AssignQ).order_by(AssignQ.id.desc()).first()
                default_variation = QuestionVariation(curr_request.col1, curr_request.col2, last_question.id)
                db.session.add(default_variation)
                db.session.commit()
                curr_request.status = Status.PASSED
                db.session.commit()
                # add new answer to the variation
                last_question_variation = db.session.query(QuestionVariation).order_by(QuestionVariation.id.desc()).first()
                new_llm_answer = LLMAnswer(curr_request.col4, curr_request.col7, last_question_variation.id)
                db.session.add(new_llm_answer)
                db.session.commit()
                # add new score to the answer
                last_llm_answer = db.session.query(LLMAnswer).order_by(LLMAnswer.id.desc()).first()
                new_llm_score = LLMScore(curr_request.col5, curr_request.col6, last_llm_answer.id, curr_request.user_id)
                db.session.add(new_llm_score)
                db.session.commit()
                flash('New question added to the database!', 'success')
                return redirect(url_for('request.view_requests'))

            if curr_request.request_type == RequestType.UPDATE_SCORE:
                new_score = LLMScore(curr_request.col2, curr_request.col3, curr_request.col1, curr_request.user_id)
                db.session.add(new_score)
                db.session.commit()
                curr_request.status = Status.PASSED
                db.session.commit()
                flash('New score and comment added to the database!', 'success')
                return redirect(url_for('request.view_requests'))

            if curr_request.request_type == RequestType.EXPERIMENT:
                # add new variation first
                new_question_variation = QuestionVariation(curr_request.col2, curr_request.col3, curr_request.col1)
                db.session.add(new_question_variation)
                db.session.commit()
                # add new answer to the variation
                last_question_variation = db.session.query(QuestionVariation).order_by(QuestionVariation.id.desc()).first()
                new_llm_answer = LLMAnswer(curr_request.col4, curr_request.col7, last_question_variation.id)
                db.session.add(new_llm_answer)
                db.session.commit()
                # add new score to the answer
                last_llm_answer = db.session.query(LLMAnswer).order_by(LLMAnswer.id.desc()).first()
                new_llm_score = LLMScore(curr_request.col5, curr_request.col6, last_llm_answer.id, curr_request.user_id)
                db.session.add(new_llm_score)
                db.session.commit()
                curr_experiment = Experiment.query.get_or_404(curr_request.col8)
                curr_experiment.status = ExperimentStatus.IN_GENERAL_DATABASE
                curr_request.status = Status.PASSED
                db.session.commit()
                flash('New score and comment added to the database!', 'success')
                return redirect(url_for('request.view_requests'))

            if curr_request.request_type == RequestType.ADD_TOPIC:
                new_topic = Helptopic(curr_request.col1, curr_request.col2, curr_request.col3, curr_request.col4,
                                         curr_request.col5, curr_request.col6)
                db.session.add(new_topic)
                db.session.commit()
                curr_request.status = Status.PASSED
                db.session.commit()

                flash('New topic added to the database!', 'success')
                return redirect(url_for('request.view_requests'))

        if decision == 'reject':
            if curr_request.request_type == RequestType.EXPERIMENT:
                curr_experiment = Experiment.query.get_or_404(curr_request.col8)
                curr_experiment.status = ExperimentStatus.NOT_SUBMITTED
            curr_request.status = Status.REJECTED
            db.session.commit()
            return redirect(url_for('request.view_requests'))

    return render_template('handle_request.html', request=curr_request)

