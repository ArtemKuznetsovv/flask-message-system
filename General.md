#Messaging System

## Open Endpoints

Open endpoints require no Authentication.

* [Authentication](Readme's/login.md) : `POST /authentication`

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

* [Write Message](Readme's/write.md) : `POST /messages/{User}`
* [Get Messages](Readme's/get.md) : `GET /messages/{User}`
* [Read message](Readme's/read.md) : `PUT /messages/{User}`
* [Delete message](Readme's/delete.md) : `DELETE /messages/{User}`