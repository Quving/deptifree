#!/bin/bash
set -e
python manage.py collectstatic
gunicorn --bind 0.0.0.0:7500 deptifree.wsgi
