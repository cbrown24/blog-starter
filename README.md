# OfficeApp Python assignment

## Assignment
```
Try to create a blog that meets the following requirements:

-   The blog has to be coupled to a database
-   The blog must contain the following components

-   Posts
-   Users
-   Topics

- The blog must be able to contain multiple topics. Each topic must be able to contain 1 or more posts. Each post has to be coupled to a user

- It must be possible to retrieve / collect all topics from the blog, to search for posts and retrieve all posts from one specific user. Additional completion is free, creativity is being appreciated

- Add Unit tests so it can be tested easily

- Include a short description (documentation) how to set up the blog

- If possible, create it in Django. Front-end is not relevant, it’s the python code that is relevant
```


## Solution
Developed in Python 3.7.5
- Is a Flask App
- Uses JWT for authentication
- SQLAlchemy for ORM
- Restplus for API marhsalling
- Initial setup with the admin user is in ./migrations/versions/c292fb06f01d_.py 
- admin user is setup with (login email=am@foo, password=admin)


## Installing
 create a venv
```
Christophers-MacBook-Pro:rabo christopherbrown$ python3 -m venv office_app
```
activate venv and clone https://github.com/cbrown24/blog-starter.git
```
Christophers-MacBook-Pro-2:office_app christopherbrown$ source bin/activate

(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ git clone https://github.com/cbrown24/blog-starter.git src

Cloning into 'src'...

remote: Enumerating objects: 62, done.

remote: Counting objects: 100% (62/62), done.

remote: Compressing objects: 100% (45/45), done.

remote: Total 62 (delta 16), reused 52 (delta 11), pack-reused 0

Unpacking objects: 100% (62/62), done.

(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ cd src/
```

pip install
```
(office_app) Christophers-MacBook-Pro-2:src christopherbrown$ pip install -r requirements.txt
Collecting alembic==1.3.2 (from -r requirements.txt (line 1))
... snip ...
```

DB setup
```
(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ pwd

/Users/christopherbrown/Documents/testing_app/office_app
### set app environment
(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ export FLASK_APP=BLOG_STARTER:app


### Now run the db migration to setup tables and the admin user
(office_app) Christophers-MacBook-Pro-2:blog-starter christopherbrown$ python manage.py db upgrade

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.

INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

INFO  [alembic.runtime.migration] Running upgrade  -> c292fb06f01d, empty message
```


## Testing Using Swagger 
Startup using
```
```
- Unfortunately due to time constraints,  automated testing is not included in this project.
- This application can be tested using the swagger UI which is available on localhost:5000/api
- Please generate a JWT Authorization token using the login endpoint.
- The response will give you an Authorization token which can be stored and used to authenticate agains other endpoints.
- Please click the authorise padlock icon in the top right hand corner of the SwaggerUI page to store this token.
- All endpoints requiring authorisation will subsequently use this token.


## Demo
use curl to create a topic
```
(office_app) Christophers-MacBook-Pro-2:blog-starter christopherbrown$ curl -X POST "http://127.0.0.1:5000/topic/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" -H "Content-Type: application/json" -d "{ \"name\": \"test_topic\"}"
```


create a post in a topic
```
curl -X POST "http://127.0.0.1:5000/post/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" -H "Content-Type: application/json" -d "{ \"title\": \"string\", \"body\": \"string\", \"topic_id\": 1}"
```

read topic
```
curl -X GET "http://127.0.0.1:5000/topic/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" 
[{
"name": "test_topic",
"created_by": null,
"created_on": null,
"posts": [
{
"created_by": "unknown",
"created_on": "2020-01-20T10:50:36.707717",
"title": "string",
"body": "string",
"topic_id": 2
}
],
"id": 2
}]
```


## Unfinished items
- add comments to blog
- unit + functional testing
- pycodestlye / pep8
