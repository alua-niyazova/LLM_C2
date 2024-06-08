from flask import Blueprint, request, render_template, redirect, url_for, flash, abort, jsonify
from sqlalchemy import or_, func
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload, aliased

from app.models.base import db
from app.models.assignQ import AssignQ
from app.models.course import Course, CourseCategory
from app.models.llmanswer import LLMAnswer
from app.models.llmscore import LLMScore
from app.models.questionVariation import QuestionVariation  # Ensure this import
from app.models.request import Request, RequestType

searchBP = Blueprint('search', __name__, url_prefix='/search')


def is_authorized():
    return current_user.is_authenticated and current_user.utype in ['Admin', 'Teacher']


@searchBP.route('/', methods=['GET'])
@login_required
def search():
    if not is_authorized():
        abort(403)

    name = request.args.get('llm_name')
    score_min = request.args.get('score_min', type=float)
    score_max = request.args.get('score_max', type=float)
    category = request.args.get('category')
    course_name_or_number = request.args.get('course_name')

    # Using aliases for clarity in joins
    question_variation_alias = aliased(QuestionVariation)
    llm_answer_alias = aliased(LLMAnswer)
    llm_score_alias = aliased(LLMScore)

    query = AssignQ.query \
        .outerjoin(question_variation_alias, AssignQ.variations) \
        .outerjoin(llm_answer_alias, question_variation_alias.answers) \
        .join(AssignQ.course) \
        .distinct()

    filters = []
    if name:
        filters.append(llm_answer_alias._LLM_Name.like(f'%{name}%'))
    if score_min is not None and score_max is not None:
        score_subquery = db.session.query(llm_score_alias.answer_id).group_by(llm_score_alias.answer_id).having(
            func.avg(llm_score_alias.score).between(score_min, score_max)
        ).subquery()
        filters.append(llm_answer_alias.id.in_(score_subquery))
    if score_min is not None and score_max is None:
        score_subquery = db.session.query(llm_score_alias.answer_id).group_by(llm_score_alias.answer_id).having(
            func.avg(llm_score_alias.score).between(score_min, 5)
        ).subquery()
        filters.append(llm_answer_alias.id.in_(score_subquery))
    if score_min is None and score_max is not None:
        score_subquery = db.session.query(llm_score_alias.answer_id).group_by(llm_score_alias.answer_id).having(
            func.avg(llm_score_alias.score).between(0, score_max)
        ).subquery()
        filters.append(llm_answer_alias.id.in_(score_subquery))
    if category:
        filters.append(Course.category == category)
    if course_name_or_number:
        try:
            course_number = int(course_name_or_number)
            filters.append(or_(Course.cName.like(f'%{course_name_or_number}%'), Course.cNumber == course_number))
        except ValueError:
            filters.append(Course.cName.like(f'%{course_name_or_number}%'))

    if filters:
        query = query.filter(*filters)

    results = query.all()
    all_courses = Course.query.all()
    return render_template('search.html', results=results, courses=all_courses, CourseCategory=CourseCategory)


@searchBP.route('/variations/<int:question_id>', methods=['GET'])
@login_required
def question_variations(question_id):
    if not is_authorized():
        abort(403)

    llm_name = request.args.get('llm_name')
    score_min = request.args.get('score_min', type=float)
    score_max = request.args.get('score_max', type=float)

    question = AssignQ.query.get_or_404(question_id)
    variations = question.variations

    filtered_variations = []
    for var in variations:
        if llm_name and not any(llm_name.lower() in ans._LLM_Name.lower() for ans in var.answers):
            continue
        if score_min is not None:
            if not any(score_min <= (db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == ans.id).scalar() or 0) for ans in var.answers):
                continue
        if score_max is not None:
            if not any((db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == ans.id).scalar() or 0) <= score_max for ans in var.answers):
                continue

        filtered_variations.append({
            "id": var.id,
            "code": var.vCode,
            "text": var.vText
        })

    return jsonify(filtered_variations)


@searchBP.route('/answers/<int:variation_id>', methods=['GET'])
@login_required
def variation_answers(variation_id):
    if not is_authorized():
        abort(403)

    llm_name = request.args.get('llm_name')
    score_min = request.args.get('score_min', type=float)
    score_max = request.args.get('score_max', type=float)

    variation = QuestionVariation.query.get_or_404(variation_id)
    answers = variation.answers
    filtered_answers = []
    for ans in answers:
        if llm_name and not llm_name.lower() in ans._LLM_Name.lower():
            continue
        if score_min is not None:
            avg_score = db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == ans.id).scalar() or 0
            if not (score_min <= avg_score):
                continue
        if score_max is not None:
            avg_score = db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == ans.id).scalar() or 0
            if not (avg_score <= score_max):
                continue

        filtered_answers.append({
            "name": ans._LLM_Name,
            "image": ans._LLMAnswerImg,
            "id": ans.id,
            "average_score": float(db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == ans.id).scalar() or 0)
        })

    return jsonify(filtered_answers)


@searchBP.route('/answer_details/<int:answer_id>', methods=['GET'])
@login_required
def answer_details(answer_id):
    if not is_authorized():
        abort(403)

    answer = LLMAnswer.query.get_or_404(answer_id)
    scores_and_comments = [
        {
            "score": score.score,
            "comment": score.comment,
        }
        for score in answer.scores
    ]
    return jsonify(scores_and_comments)


@searchBP.route('/answers_json/<int:question_id>', methods=['GET'])
@login_required
def answers_json(question_id):
    if not is_authorized():
        abort(403)

    question = AssignQ.query.get_or_404(question_id)
    answers = [
        {"name": ans._LLM_Name, "score": ans._LLM_Score, "comment": ans._comments, "image": ans._LLMAnswerImg,
         "id": ans._answerID}
        for ans in question.answers
    ]
    return jsonify(answers)


@searchBP.route('/answers/update/<int:answer_id>', methods=['GET', 'POST'])
@login_required
def update_score(answer_id):
    if not is_authorized():
        abort(403)

    answer = LLMAnswer.query.get_or_404(answer_id)
    if request.method == 'POST':
        comment = request.form.get('comment')
        score = request.form.get('score', type=int)

        if not comment or score is None:
            flash('Missing inputs.', 'error')
            return redirect(url_for('search.update_score', answer_id=answer_id))

        if score > 5 or score < 0:
            flash('Invalid value for score.', 'error')
            return redirect(url_for('search.update_score', answer_id=answer_id))

        # Check if the current user has already submitted a request for this answer
        existing_request = Request.query.filter_by(
            col1=str(answer_id),
            user_id=current_user.id,
            request_type=RequestType.UPDATE_SCORE
        ).first()

        if existing_request:
            flash('You have already submitted a score update request for this answer.', 'info')
            return redirect(url_for('search.search'))

        # Submit a new score update request
        new_request = Request(
            request_type=RequestType.UPDATE_SCORE,
            user_id=current_user.id,
            col1=str(answer.id),
            col2=str(score),
            col3=comment
        )
        db.session.add(new_request)
        db.session.commit()
        flash('Score update request submitted!', 'success')
        return redirect(url_for('search.search'))

    return render_template('update_answer.html', answer=answer)
