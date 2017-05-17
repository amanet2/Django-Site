# Django-Site
In action: ![screen](screen.jpg?raw=true "Oscreen")

Requirements
===
* Python3.6
* (windows) Python3.6 must be on your path

Quick Instructions
===
## Quickstart
1. Run `quickstart_setup.bat` and complete the admin setup
1. Run `quickstart_runserver.bat`

## Use Case
1. Goes to `localhost:8000/admin` and login
1. Creates a new Map called `topdown_template` and saves
1. Goes to `localhost:8000/scenebuilder`
1. Finds the `topdown_template` map and clicks `download`
1. `topdown_template.map` will start to download

## Use Case
1. Goes to `localhost:8000` and clicks on scenebuilder app
1. Goes to the `Build your own` tab on top navbar
1. Selects some scenery, actors, etc and places them on the grid

## Use Case
1. Uses Game-Engine-Red/Map-File-Writer
1. Generates mapfile `custom.map`
1. Adds it to the `basesite/downloadable_maps` folder
1. Goes to `localhost:8000/admin` and login
1. Creates a new Map called `custom` and saves
1. Goes to `localhost:8000/scenebuilder`
1. Finds the `custom` map and clicks `download`
1. `custom.map` will start to download

## More instructions
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
