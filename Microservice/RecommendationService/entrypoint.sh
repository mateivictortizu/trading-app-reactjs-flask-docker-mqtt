#!/bin/bash
gunicorn --bind 0.0.0.0:5006 wsgi:application