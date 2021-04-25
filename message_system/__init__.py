import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config['SECRET_KEY'] = "secret"

    USERNAME = "postgres"
    PASSWORD = "Elb7302it!"
    HOST_NAME = "localhost"
    DB_NAME = "herolotask"

    #os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USERNAME}:{PASSWORD}@{HOST_NAME}:5432/{DB_NAME}"
    db.init_app(app)

    from message_system.models import User, Message
    with app.app_context():
        db.create_all()
        db.session.commit()

    from message_system import routes
    return app






