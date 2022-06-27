#!/bin/bash
gunicorn --bind 0.0.0.0:5000 -k gevent -w 1 wsgi:app