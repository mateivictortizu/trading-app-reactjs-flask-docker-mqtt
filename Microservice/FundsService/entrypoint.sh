#!/bin/bash
flask db init
flask db migrate
flask db upgrade
gunicorn --bind 0.0.0.0:5002 wsgi:app --log-level debug