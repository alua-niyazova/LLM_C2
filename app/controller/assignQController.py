import os

from flask import Blueprint, request, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.models.base import db
from app.models.assignQ import AssignQ
from app.models.course import Course
from app.models.request import Request, RequestType

assignQBP = Blueprint('assignQ', __name__, url_prefix='/assignq')


def is_authorized():
    return current_user.is_authenticated and current_user.utype in ['Admin', 'Teacher']


@assignQBP.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if not is_authorized():
        abort(403)

    courses = Course.query.all()  # fetch all courses to be displayed (dropdown menu selection)
    if request.method == 'POST':
        qcode = request.form.get('qcode')
        qtext = request.form.get('qtext')
        course_id = request.form.get('course_id')
        llm_name = request.form.get('LLM_name')
        score = request.form.get('score', type=int)
        comment = request.form.get('comment')
        print(request.form)

        if not qcode or not qtext or not course_id or not llm_name or not score or not comment:
            flash('All fields are required.', 'error')
            return redirect(url_for('assignQ.add_question'))

        if score > 5 or score < 0:
            flash('Invalid value for score.', 'error')
            return redirect(url_for('assignQ.add_question'))

        from ourwork import app

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
            return redirect(url_for('assignQ.add_question'))

        new_question_request = Request(
            request_type=RequestType.ADD_QUESTION,
            user_id=current_user.id,
            col1=str(qcode),
            col2=str(qtext),
            col3=str(course_id),
            col4=llm_name,
            col5=str(score),
            col6=comment,
            col7=answer_img
        )

        db.session.add(new_question_request)
        db.session.commit()
        flash('New question request submitted!', 'success')
        return redirect(url_for('assignQ.add_question'))

    return render_template('add_question.html', courses=courses)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
