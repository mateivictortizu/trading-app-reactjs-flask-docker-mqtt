#!/bin/bash
flask db init
flask db migrate
flask db upgrade
gunicorn --bind 0.0.0.0:5005 wsgi:app