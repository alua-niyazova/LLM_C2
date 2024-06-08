import os

from flask import Blueprint, request, render_template, redirect, url_for, flash, abort, jsonify
from sqlalchemy import or_, func
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.models.base import db
from app.models.assignQ import AssignQ
from app.models.course import Course
from app.models.experiment import Experiment, ExperimentStatus
from app.models.llmanswer import LLMAnswer
from app.models.llmscore import LLMScore
from app.models.questionVariation import QuestionVariation  # Ensure this import
from app.models.request import Request, RequestType


expBP = Blueprint('exp', __name__, url_prefix='/exp')


def is_authorized():
    return current_user.is_authenticated and current_user.utype in ['Admin', 'Teacher']


@expBP.route('/', methods=['GET'])
@login_required
def view_exp():
    if not is_authorized():
        abort(403)

    user_exps = Experiment.query.filter_by(user_id=current_user.id).all()
    return render_template('all_exps.html', exps=user_exps)


@expBP.route('/exp_request/<int:exp_id>', methods=['GET'])
@login_required
def exp_request(exp_id):
    if not is_authorized():
        abort(403)

    experiment = Experiment.query.get_or_404(exp_id)
    new_request = Request(
        request_type=RequestType.EXPERIMENT,
        user_id=current_user.id,
        col1=str(experiment.question_id),
        col2=experiment.vCode,
        col3=experiment.vText,
        col4=experiment.LLM_name,
        col5=str(experiment.score),
        col6=experiment.comment,
        col7=experiment.answer_img,
        col8 = experiment.id
    )
    experiment.status = ExperimentStatus.SUBMITTED
    db.session.add(new_request)
    db.session.commit()
    flash('Adding into general database request submitted!', 'success')
    return redirect(url_for('exp.view_exp'))


@expBP.route('/upload/<int:question_id>', methods=['GET', 'POST'])
@login_required
def exp_upload(question_id):
    if not is_authorized():
        abort(403)

    from ourwork import app

    question = AssignQ.query.get_or_404(question_id)
    if request.method == 'POST':
        # Retrieve text data
        v_code = request.form.get('vCode')
        v_text = request.form.get('vText')
        llm_name = request.form.get('LLM_name')
        comment = request.form.get('comment')
        score = request.form.get('score', type=int)

        # Check for required inputs
        if not v_code or not v_text or not llm_name or not comment or score is None:
            flash('Missing inputs.', 'error')
            return redirect(url_for('exp.exp_upload', question_id=question_id))

        # Score validation
        if score > 5 or score < 0:
            flash('Invalid value for score.', 'error')
            return redirect(url_for('exp.exp_upload', question_id=question_id))

        # Handle file upload
        file = request.files.get('answer_img')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.static_folder, filename)
            file.save(file_path)
            answer_img = os.path.join(app.static_folder, filename)
            answer_img = os.path.join('/images', os.path.basename(answer_img))
        else:
            flash('No valid image provided', 'error')
            return redirect(url_for('exp.exp_upload', question_id=question_id))

        # Create new experiment
        new_experiment = Experiment(
            question_id=question_id,
            vCode=v_code,
            vText=v_text,
            LLM_name=llm_name,
            score=score,
            comment=comment,
            answer_img=answer_img,
            user_id=current_user.id
        )
        db.session.add(new_experiment)
        db.session.commit()
        flash('New experiment uploaded!', 'success')
        return redirect(url_for('exp.view_exp'))

    return render_template('upload_exp.html', question=question)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
