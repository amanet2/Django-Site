# Django-Site
In action: ![screenm](screen.jpg?raw=true "Oscreen")
Quick Instructions
===
## Create Virtual Environment

### INTELLIJ/PYCHARM: 
1. Start new project, and create virtualenv when selecting
  Python3.6 SDK.  
1. Point to this source during the project name selection step.
1. Install requirements from `requirements.txt`

### CMD:
1. Make sure Python3.6 is on your path
1. `virtualenv venv` where `venv` can be any name
1. `venv\Scripts\activate`

## Install Requirements

### INTELLIJ/PYCHARM
1. IDE should prompt you to install requirements from `requirements.txt`

### CMD:
1. Navigate to project dir
1. `pip install -r requirements.txt`

## Make Migrations

### INTELLIJ/PYCHARM
1. Create Run configuration `python manage.py migrate`

### CMD:
1. `python manage.py migrate`

## Run Program

### INTELLIJ/PYCHARM
1. Create Run configuration `python manage.py runserver`

### CMD:
1. `python manage.py runserver`

## In your brower, navigate to `localhost:8000`
