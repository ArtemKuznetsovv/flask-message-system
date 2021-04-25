# Get Messages

Get messages that was sent to the authenticated user

**URL** : ``/messages/{User}``

**Method** : `GET`

**Auth required** : YES

### Data constraints

**In the url provide**: an authenticated username

**In the headers provide**:"Authorization" header

**Optional (In the URL):**
 
   `read=false` (provide false for unread messages and nothing for all messages)


**Example** 
[messages/Artem](https://flask-message-system.herokuapp.com/messages/ArtemTest)

## Success Response

**Condition** : The user is authenticated and there are matching queries in the DataBase

**Code** : `200 OK`

**Content example**

```json
{
    "data": [
        {
            "content": "self-message",
            "date": "2021-04-25 15:53:25.842871",
            "read": "False",
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

**Condition** : If fields are missed.

**Code** : `404 NOT FOUND`

**Content example**

```json
{"error": "No messages for this specific query"}
```

* ### Notes

    **The endpoints get all messages for a specific user, and get all unread messages for a specific user 
are combined in this one endpoint**
    **Also note that you can get only messages that are meant for you**
