from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

from app.models.base import db

from app.controller import topicController, courseController, searchController, \
    assignQController, userController, requestController, experimentController
from app import create_app

app = create_app()


mail = Mail(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

if __name__ == '__main__':
    # 启动应用服务器, 我们使用本地
    app.run(debug=True, host='127.0.0.1', port=5000)
    # app.run(host='0.0.0.0', port=5001)

