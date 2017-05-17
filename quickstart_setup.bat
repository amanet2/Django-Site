cmd /k "virtualenv venv & venv\Scripts\activate & pip install -r basesite/requirements.txt & python basesite/manage.py migrate & python basesite/manage.py createsuperuser & deactivate"
