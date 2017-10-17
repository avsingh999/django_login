# django_login
Custom login api build on the top of Django auth app.

[![Build Status](https://www.travis-ci.org/mohitkyadav/algos-ngular.svg?branch=master)](https://travis-ci.org/mohitkyadav/django_login)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/mohitkyadav/django_login)

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/SolidScript/django_login)

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
