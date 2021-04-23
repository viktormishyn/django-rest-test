#!/bin/bash

sudo apt install libpq-dev
python3 -m venv env
source env/bin/activate

if [ ! -f "requirements.txt" ]; then
  echo "Installing requirements and creating requirements.txt..."
  echo
  pip install wheel
  pip install django
  pip install djangorestframework
  pip install autopep8
  pip freeze > requirements.txt
else
  echo "Found requirements.txt. Installing requirements..."
  pip install -r requirements.txt
fi

code .
