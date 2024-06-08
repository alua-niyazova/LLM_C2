from app.controller import userController, requestController, courseController, assignQController, searchController, \
    experimentController, topicController,experiment


def init_app_routes(app):

    app.register_blueprint(userController.userBP, url_prefix='/')
    app.register_blueprint(requestController.requestBP, url_prefix='/request')
    app.register_blueprint(courseController.courseBP, url_prefix='/course')
    app.register_blueprint(assignQController.assignQBP, url_prefix='/assignq')
    app.register_blueprint(searchController.searchBP, url_prefix='/search')
    app.register_blueprint(experimentController.expBP, url_prefix='/exp')
    app.register_blueprint(topicController.topicBP, url_prefix='/topic')
    app.register_blueprint(experiment.experiment_bp, url_prefix='/experiment')
