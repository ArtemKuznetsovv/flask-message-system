# Create A Message

Create a Message from the authenticated user

**URL** : ``/messages/{User}``

**Method** : `POST`

**Auth required** : YES

**Data constraints**

**In the body provide**:
receiver name, message content, message subject

**In the headers provide**:"Authorization" header

**In the url provide**: an authenticated username


```json
{
    "receiver": "{string}",
    "content": "{string}",
    "subject": "{string}"
}
```

**Data example** All fields must be sent.

```json
{
    "receiver": "Quentin Tarantino",
    "content": "Hello",
    "subject": "Greetings"
}
```

**Example** 
https://flask-message-system.herokuapp.com/messages/ArtemTest

## Success Response

**Condition** : If user attached his token in headers and the sender field is the same as the user that makes the request.

**Code** : `201 CREATED`

**Content example**

```json
{
    "message": "Your message has been submitted successfully"
}
```

## Error Responses

**Condition** : If User not authenticated.

**Code** : `401 Unathorized`


### Or

**Condition** : If fields are missed.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "message": "Request JSON is missing some required params",
    "missing": [
        "subject"
    ],
    "status": "error"
}
```

