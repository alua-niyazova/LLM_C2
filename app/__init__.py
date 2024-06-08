from flask import Flask

from app.controller import topicController, courseController, \
    searchController, \
    assignQController, userController, requestController, experimentController
from app.models.user import User


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


from flask_login import LoginManager
login_manager = LoginManager()

def setup_login_manager(app):
    login_manager.init_app(app)

    from app.models.user import User

    login_manager.login_view = 'user.login'
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__, static_folder='images', static_url_path='/images')

    app.config.from_object('app.config.secure')

    app.config['SECRET_KEY'] = "b'Ly\x00a\xfe\\\xde\xc5\xe0xB\xe5\xd0_d*\xc3)\x05\xcf\x80:\xd2\x89'"

    app.config['MAIL_SERVER'] = 'smtp.qq.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = '2920855906@qq.com'
    app.config['MAIL_PASSWORD'] = 'hrvpymkplnxzdfgf'
    app.config['MAIL_DEFAULT_SENDER'] = '2920855906@qq.com'

    # max 16MB for image upload
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    from app.models import user  # Import models
    from app.routes import init_app_routes  # Import a function to initialize routes

    register_plugin(app)

    init_app_routes(app)  # Setup routes

    setup_login_manager(app)

    return app
