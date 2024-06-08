import os

from flask import Blueprint, render_template, request, jsonify, url_for, flash, abort
from flask import Flask, render_template, jsonify, request, redirect

from app.controller.assignQController import allowed_file
from app.models.base import db

from werkzeug.utils import secure_filename
from app.models.helpTopic import Helptopic
from app.models.course import Course  # 确保导入Course模型
from flask_login import login_required, current_user
from app.models.request import Request, RequestType

topicBP = Blueprint('topic', __name__)  # 创建一个蓝图，将其绑定到app上

def is_authorized():
    return current_user.is_authenticated and current_user.utype in ['Admin', 'Student']

@topicBP.route('/add_topic', methods=['GET', 'POST'])
@login_required
def add_topic():
    if not is_authorized():
        abort(403)
    courses = Course.query.all()
    if request.method == 'POST':
        topic = request.form.get('topic')
        subtopic = request.form.get('subtopic')
        ttext = request.form.get('ttext')
        category = request.form.get('category')
        course_id = request.form.get('course_id')


        if not topic or not subtopic or not category or not ttext or not course_id:
            flash('All fields are required.', 'error')
            return redirect(url_for('topic.add_topic'))

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
            return redirect(url_for('topic.add_topic'))

        new_topic_request = Request(
            request_type=RequestType.ADD_TOPIC,
            user_id=current_user.id,
            col1=str(topic),
            col2=str(subtopic),
            col3=str(category),
            col4=str(ttext),
            col5=str(answer_img),
            col6=str(course_id),
        )
        db.session.add(new_topic_request)
        db.session.commit()
        flash('New topic request submitted!!', 'success')
        return redirect(url_for('topic.add_topic'))

    return render_template('add_topic.html', courses=courses)


@topicBP.route('/topicsearch', methods=['GET', 'POST'])
def topicsearch():
    content = request.form.get('content', '').strip()  # 获取表单数据，并去除两边空白字符

    if content:  # 确保只有当content非空时执行查询
        # 通过关联的Course对象的cName字段进行搜索
        # 注意这里我们需要引入Course模型，并通过join实现关联查询

        quotes = Helptopic.query.join(Course).filter(Course.cName.ilike(f"%{content}%")).all()
    else:
        quotes = []  # 如果搜索内容为空，返回空列表以避免展示所有记录

    return render_template('topicsearch.html', quotes=quotes)



@topicBP.route('/get_coursetypes')
def get_coursetypes():
    coursetypes = Helptopic.query.with_entities(Helptopic.coursetype).distinct().all()
    return jsonify([{'name': ct.coursetype} for ct in coursetypes])

@topicBP.route('/get_topics/<string:coursetype>')
def get_topics(coursetype):
    topics = Helptopic.query.filter_by(coursetype=coursetype).distinct().all()  # Ensure distinct is correctly used
    return jsonify([{'name': topic.topic} for topic in topics])


@topicBP.route('/get_subtopics/<string:topic>')
def get_subtopics(topic):
    subtopics = Helptopic.query.filter_by(topic=topic).distinct().all()
    return jsonify([{'name': subtopic.subtopic} for subtopic in subtopics])

@topicBP.route('/get_helptopics/<string:subtopic>')
def get_helptopics(subtopic):
    helptopics = Helptopic.query.filter_by(subtopic=subtopic).all()
    return jsonify([{'question': ht.topicq, 'answer': ht.topica} for ht in helptopics])
