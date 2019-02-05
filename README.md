# Deptifree
A fun project written in python using django.

[![Build Status](https://drone.quving.com/api/badges/Quving/deptifree/status.svg)](https://drone.quving.com/Quving/deptifree)

## What's Deptifree?
Deptifree is an application that manages smartly your depts at your friends. By providing a well design overview you know everytime and everywhere about your financial status.


## What's in this repository?
This repository provides the whole RestApi-Backend of Deptifree written in Python.

## Setup
1. ```git clone git@github.com:Quving/deptifree.git ```
2. ``` cd deptifree ```
3. ``` pip install -r requirements.txt ```
4. Set required system environment variables like described below.
5. ``` python manage.py runserver ```

### Environment Variables
Add these to ```~/.bashrc ``` (Linux), or ```~/.bash_profile``` (Mac)

```
export MYSQL_DB="deptifree"
export MYSQL_USER="deptifree"
export MYSQL_PASSWORD="mybestpassword"
export MYSQL_HOST="myhost.com"
export MYSQL_PORT="3300"
export EMAIL_HOST='in-v3.mailjet.com'
export DEFAULT_FROM_EMAIL='example@myhost.com'
export EMAIL_PORT=587
export EMAIL_HOST_USER='some_client_id'
export EMAIL_HOST_PASSWORD='some_client_secret'
```

## Register user
To be able to perform CRUD-Operations on the entities, the user should be registred.

Example POST-request using curl:
```
curl -X POST --header 'Content-Type: application/json' \
--header 'Accept: application/json' -d \
'{  
   "username": "myusername", \ 
   "email": "my@awesome.email", \ 
   "password1": "mypassword!", \ 
   "password2": "mypassword!" \ 
 }' 'http://localhost:8000/account/registration/'
 
```


## API-Documentation
The swagger documentation can be found here.
http://localhost:8000/docs/swagger
