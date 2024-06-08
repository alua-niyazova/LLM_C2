from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from app.models.Topic_experiment import Topic_experiment
from app.models.base import db

experiment_bp = Blueprint('experiment', __name__)


@experiment_bp.route('/add', methods=['POST'])
def save_experiment():
    if request.method == 'GET':
        return render_template('.html')
    elif request.method == 'POST':
        data = request.get_json()  # 从请求中获取 JSON 数据

        # 检查请求数据是否包含所有必需的字段
        if not all(key in data for key in ['vTxt', 'LLMused', 'answerImage', 'score']):
            return jsonify({'error': 'Missing required fields'}), 400

        # 从数据中提取字段
        vTxt = data['vTxt']
        LLMused = data['LLMused']
        answer = data['answerImage']
        score = data['score']
        print("Received data:", data)
        print("Extracted - vTxt:", vTxt, "LLMused:", LLMused, "Answer:", answer, "Score:", score)
        #
        # 尝试创建新的实验记录并保存到数据库
        try:
            # 使用实验模型创建实例
            experiment = Topic_experiment(vTxt=vTxt, LLMused=LLMused, answer=answer, score=score)
            # 添加实例到会话中
            db.session.add(experiment)
            # 提交事务
            db.session.commit()
        except Exception as e:
            # 出错时回滚事务
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

        # 返回成功响应
        response = {'message': 'Experiment added successfully'}
        return jsonify(response), 201

# @experiment_bp.route('/experiments/submit', methods=['POST'])
# def submit_experiment():
#     data = request.get_json()
#     experiment = Experiment.query.filter_by(eid=data['eid']).first()
#     if experiment:
#         # 伪代码：提交到通用数据集的逻辑
#         # 实际应用需要与管理员的审核系统接口
#         return jsonify({'message': 'Submission requested successfully'}), 200
#     else:
#         return jsonify({'message': 'Experiment not found'}), 404

@experiment_bp.route('/get', methods=['GET'])
def get_experiments():
    # 获取数据库中的所有实验记录
        experiments = Topic_experiment.query.all()

    # 将每个实验记录转换为字典
        experiments_list = [
            {
                'eid': exp.eid,
                'vTxt': exp.vTxt,
                'LLMused': exp.LLMused if exp.LLMused is not None else "NULL",
                'answer': exp.answer,
                'score': exp.score
            }
            for exp in experiments
        ]

        # 返回实验记录列表作为 JSON 响应
        return render_template('all_experiments.html', experiments=experiments_list)


@experiment_bp.route('/flash_message', methods=['POST'])
def flash_message():
    flash('Successful submit', 'success')
    return render_template('all_experiments.html')
