# Survey-Application
Simple Survey Web application with Django and VUE.JS


## Key Feature
  - Survey Publisher and Audience Management.
  - REST-API Integrated(No auth).
  - Survey Dispatch through E-mail Support.
  - Survey with short description management to announce purpose of that survey.
  - Record Tracking for submited Survey for Publisher and User
  - No Package (like Django Poll app) integration 
  - Question setup was based on eveyone can serve their need like yes/no to 10 option's for a question is allowed.
  - Each time one option to choose for a user to easily submit the Survey.
  - Error and Alert using Vue.JS to support Interactive UI.


## Survey Publisher Privilege

Application Build with a lots more concentration to give a publisher easy Survey control management through user friendly interface.

- Multi Publisher supported Survey Title with short description management where visitor can check those Survey without Login to visualized the need of the Survey.
- Questionnaire Management for a specific Survey is Very friendly to ask any kind of question from Yes/No,True/False,review collection like avarage,good,very good,excellent.
- Dispatch Any survey to a centain value added audience to attract and the mail contain the survey question
- Report Managment for Keep track of Every survey 
- One Publisher Survey category never showed to another publisher.

## Audience Privilege
- Visitor can check Survey with all publisher.
- Easy Signup process with Auto login during signup.
- Just Login and submit any Survey.
- Result Showing Facility for user to check in future about their Answer.

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/E-Rdiagram-1.jpg" height=400px width="800"/>

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/1610895407390.png" height=400px width="800"/>

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/1610895407390.png" height=400px width="800"/>

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/1610809460461.png" height=600px width="800"/>


For mail Configuration Please change Settings.py
- EMAIL_HOST = 'smtp.mailtrap.io'
- EMAIL_HOST_USER = '6f31b547070095'
- EMAIL_HOST_PASSWORD = 'ad2e1bfdd54d9b'
- EMAIL_PORT = '2525'

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/1610885204161.png" height=400px width="800"/>

For Run this Application:(dev env -Pycharm,Django 3.1,Python-3.7.7,SQLITE)

- git clone -b dev01 https://github.com/shoaib0906/Survey-Application.git
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- Generate a new secret key
- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py runserver

## REST-API::

After - $ python manage.py runserver you can access a simple REST-API which is integrated in this application from 

- http://127.0.0.1:8000/surveyapi/

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/api.png" height=600px width="1000"/>


## Report

<img src="https://github.com/shoaib0906/Survey-Application/blob/main/report.png" height=600px width="700"/>


## Code of Conduct

In order to ensure that the Django community is welcoming to all.



