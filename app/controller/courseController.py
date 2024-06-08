from flask import Blueprint, request, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.models.base import db
from app.models.course import Course, CourseCategory
from app.models.request import Request, RequestType

courseBP = Blueprint('course', __name__, url_prefix='/course')


def is_authorized():
    return current_user.is_authenticated and current_user.utype in ['Admin', 'Teacher']


@courseBP.route('/all', methods=['GET'])
@login_required
def list_courses():
    if not is_authorized():
        abort(403)

    courses = Course.query.all()
    return render_template('course_list.html', courses=courses, CourseCategory=CourseCategory)


@courseBP.route('/add', methods=['GET', 'POST'])
@login_required
def add_course():
    if not is_authorized():
        abort(403)

    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        category = request.form.get('category')

        if not name or not number or not category:
            flash('All fields are required.', 'error')
            return redirect(url_for('course.add_course'))

        new_course_request = Request(
            request_type=RequestType.ADD_COURSE,
            user_id=current_user.id,
            col1=str(name),
            col2=str(number),
            col3=str(category)
        )
        db.session.add(new_course_request)
        db.session.commit()
        flash('New course request submitted!!', 'success')
        return redirect(url_for('course.list_courses'))

    return render_template('add_course.html')
