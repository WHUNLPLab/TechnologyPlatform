from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


def register_blueprints(app):
    from application.controller.ans_gen import ans_gen_blueprint
    from application.controller.dialogue import dialogue_blueprint
    from application.controller.graph import graph_blueprint
    from application.controller.intention import intention_blueprint
    from application.controller.reading_comp import reading_comp_blueprint
    from application.controller.sentiment import sentiment_blueprint
    from application.controller.song_copy import song_copy_blueprint
    from application.controller.word_extraction import word_extraction_blueprint
    from application.controller.main import main_blueprint
    # Register  blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(ans_gen_blueprint)
    app.register_blueprint(dialogue_blueprint)
    app.register_blueprint(graph_blueprint)
    app.register_blueprint(intention_blueprint)
    app.register_blueprint(reading_comp_blueprint)
    app.register_blueprint(sentiment_blueprint)
    app.register_blueprint(song_copy_blueprint)
    app.register_blueprint(word_extraction_blueprint)
