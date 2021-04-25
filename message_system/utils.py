
def build_response_from_query(query):
    response = {"data": []}
    code = 200
    for entry in query:
        response["data"].append(message_to_dict(entry, exclude=['id']))

    if len(response["data"]) == 0:
        response = {"error": "No messages for this specific query"}
        code = 404

    return response, code


def message_to_dict(message, exclude=None):
    message_dict = {}
    for column in message.__table__.columns:
        message_dict[column.name] = str(getattr(message, column.name))

    for entry in exclude:
        message_dict.pop(entry, None)

    return message_dict
