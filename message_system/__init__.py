import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.debug = True

    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config['SECRET_KEY'] = "secret"

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    db = SQLAlchemy(app)

    from message_system.models import User, Message
    db.create_all()
    db.session.commit()
    return app, db


app, db = create_app()
from message_system import routes

