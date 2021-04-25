from flask import request, jsonify, Blueprint
from message_system.utils import build_response_from_query
from message_system import db, app
from message_system.models import Message, User
from message_system.validations import validate_json, validate_body_params, validate_token


@app.route("/authenticate", methods=['POST'])
@validate_json
@validate_body_params("username")
def login():
    """
    Authenticates a user based on JWT token
    using his username which is provided
    :return: Json object with the token
    """
    request_data = request.get_json()
    username = request_data["username"]
    user = User.query.filter_by(username=username).first()
    response = {}
    if user is None:
        try:
            token = User.generate_token(username)
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
            code = 200
            response["message"] = "You have been successfully authenticated"
            response["token"] = token
        except Exception as e:
            response["error"] = "An error has occurred while generating auth token\n" \
                                f"original error is {e}"
            code = 500

    else:
        response["error"] = "The username provided already exists"
        code = 409

    return jsonify(response), code


@app.route("/messages/<string:username>", methods=['POST'])
@validate_json
@validate_token
@validate_body_params("sender", "receiver", "content", "subject")
def send_message(username):
    """
    Create a message and insert to db based on body parameters
    :return: Json response
    """
    request_data = request.get_json()
    sender = request_data["sender"]
    receiver = request_data["receiver"]
    content = request_data["content"]
    subject = request_data["subject"]

    if sender != username:
        return jsonify({"error": "You can only send messages from the username which is bound to the token"}), 403

    message = Message(sender=sender, receiver=receiver, content=content, subject=subject)
    db.session.add(message)
    db.session.commit()

    response = {"message": "Your message has been submitted successfully"}
    return jsonify(response), 200


@app.route("/messages/<string:username>", methods=['GET'])
@validate_token
def get_messages(username):
    """
    Gets messages that was meant for a specific user
    Only if the user is authenticated
    :return: Json Object that represents all messages
    """
    read = request.args.get('read', default=None)
    if read is not None and read.lower() == "false":
        read = False
        messages = Message.query.filter_by(receiver=username, read=read).all()
    else:
        messages = Message.query.filter_by(receiver=username).all()
    response, code = build_response_from_query(messages)
    return jsonify(response), code


@app.route("/messages/<string:username>", methods=['PUT'])
@validate_token
def read_message(username):
    """
    Reads a message that was meant for a specific user
    Only if the user is authenticated
    :return: Json Object that represents the read message
    """

    message_id = request.args.get("id")
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        response = {"error": "This message doesn't exist"}
        code = 404
    elif message.receiver != username:
        response = {"error": "You are not allowed to read this message as you are not the receiver"}
        code = 403
    else:
        message.read = True
        message = (message,)
        db.session.commit()
        response, code = build_response_from_query(message)
    return jsonify(response), code


@app.route("/messages/<string:username>", methods=['DELETE'])
@validate_token
def delete_message(username):
    """
    Deletes a message only if the user requesting is authenticated
    and he is the sender or the receiver of the message
    :return: Json Object that represents the response
    """
    response = {}
    message_id = request.args.get("id")
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        response = {"error": "This message doesn't exist"}
        code = 404
    elif message.receiver != username and message.sender != username:
        response["error"] = "You are not allowed to delete this message" \
                            "as you are not the sender nor the receiver"
        code = 403
    else:
        db.session.delete(message)
        db.session.commit()
        response["info"] = "Message has been deleted successfully"
        code = 200

    return jsonify(response), code


if __name__ == '__main__':
    app.run()
