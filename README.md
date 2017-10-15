# django_login
Custom login api build on the top of Django auth app.


## login
navigate to http://localhost:8000/auth/login and fill out the post response with a JSON object,
```
{
    "username": "only4",
    "password": "test1234"
}
```
and hit the post button.

## confirmation of login
navigate to http://localhost:8000/your_name/cards and you'll see a json response with some objects

## logout
navigate to http://localhost:8000/auth/logout and you'll see an accept response


## confirmation of logout
navigate to http://localhost:8000/your_name/cards and you'll see a json response with an error.
