# Delete Message

Delete the given message from the database

**URL** : ``/messages/{User}``

**Method** : `DELETE`

**Auth required** : YES

###Data constraints

**In the url provide**: an authenticated username


**Example** 
[messages/Artem](https://flask-message-system.herokuapp.com/messages/ArtemTest?id=1)

## Success Response

**Condition** : The user is authenticated, the message exists and the user is the receiver or sender of the message 

**Code** : `200 OK`

**Content example**

```json
{
    "info": "Message has been deleted successfully"
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

**Condition** : User is not the receiver or the sender of the message.

**Code** : `403 Forbidden`

**Content example**

```json
{
    "error": "You are not allowed to delete this message as you are not the sender nor the receiver"
}
```