from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config="default"):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    db.init_app(app)
    ma.init_app(app)

    # Import and register blueprints
    from app.routes.comments import comment_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(comment_bp)
    app.register_blueprint(task_bp)

    return app
