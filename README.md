# DRF polls api

## Installation

Polls requires [Django](https://docs.djangoproject.com/en/2.2/) v2.2 to run.

Clone repo
```sh
git clone https://github.com/TilekTekinov/DRF-polls-api.git
cd DRF-polls-api
```

For production environments...

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create database and change database config in ```poll_app/settings.py```
```sh
python manage.py makemigrations
python manage.py migrate
```

Run server

```
python manage.py runserver
```

## API links

| Method | Link | Description |
| ------ | ------ |------ |
| ```GET``` | ```/api/polls/``` | get all polls list |
| ```POST``` | ```/api/polls/``` | create new poll |
| ```GET``` | ```/api/polls/<int:pk>/``` | get detail poll |
| ```PUT``` | ```/api/polls/<int:pk>/``` | update poll |
| ```DELETE``` | ```/api/polls/<int:pk>/``` | delete poll |
| ```GET``` | ```/api/polls/<int:pk>/questions/``` | get all questions list |
| ```POST``` | ```/api/polls/<int:pk>/questions/``` | create new question |
| ```GET``` | ```/api/polls/<int:polls_pk>/questions/<int:pk>/``` | get detail question |
| ```PUT``` | ```/api/polls/<int:polls_pk>/questions/<int:pk>/``` | get detail poll |
| ```DELETE``` | ```/api/polls/<int:polls_pk>/questions/<int:pk>/``` | delete question |
| ```GET``` | ```/api/active-polls/``` | get only active polls |
| ```POST``` | ```/api/polls/<int:polls_pk>/questions/<int:question_pk>/answer/``` | create new answer |
| ```GET``` | ```/api/answers/<int:user_pk>/``` | get all user answers |