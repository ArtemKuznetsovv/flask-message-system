

**Authenticate**
----
  Authenticate a user based on his username

* **URL**

  /authentication

* **Method:**
  
  `POST`
  

* **Body Params**

     **Required:**
 
   `username=[string]`
    
   
        {"username" = "Michael Bloom"}

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:**
   ```json
{
    "message": "You have been successfully authenticated",
    "token": "ResponseToken"
}
```

 
* **Error Response:**

  * **Code:** 409 Conflict <br />
    **Content:** `{ "error" : "The username provided already exists" }`

 
 * **Notes**
 
    **You can't authenticate more then one time**