# Read Message

Mark a message that was meant for the authenticated user as read

**URL** : ``/messages/{User}``

**Method** : `PUT`

**Auth required** : YES

###Data constraints

**In the url provide**: an authenticated username and query parameter for message ID




**Example** 
https://flask-message-system.herokuapp.com/messages/ArtemTest?id=1

## Success Response

**Condition** : The user is authenticated, the message exists and the user is the receiver of the message 

**Code** : `200 OK`

**Content example**

```json
{
    "data": [
        {
            "content": "self-message",
            "date": "2021-04-25 15:53:25.842871",
            "read": "True",
            "receiver": "ArtemTest",
            "sender": "ArtemTest",
            "subject": "testmessage"
        }
    ]
}
```

## Error Responses

**Condition** : If User not authenticated.

**Code** : `401 Unathorized`


### Or

**Condition** : If message doesn't exist.

**Code** : `404 NOT FOUND`

**Content example**

```json
{"error": "No messages for this specific query"}
```

### Or

**Condition** : If message doesn't exist.

**Code** : `403 Forbidden`

**Content example**

```json
{
    "error": "You are not allowed to read this message as you are not the receiver"
}
```

