import datetime
from message_system import db,app
import jwt


class Message(db.Model):

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    receiver = db.Column(db.String)
    content = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    read = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Message by: {self.sender} to {self.receiver}, sent at {self.date} with subject of {self.subject}" \
               f" and content of {self.content}"


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    @staticmethod
    def generate_token(username):
        payload = {'iat': datetime.datetime.utcnow(), 'sub': username}
        return jwt.encode(payload, app.config['SECRET_KEY'])

    @staticmethod
    def decode_auth_token(auth_token):
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'], "HS256")
        return payload['sub']
