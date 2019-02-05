#!/bin/bash
set -e
echo 'yes' | python manage.py collectstatic --clear
gunicorn -c gunicorn_config.py deptifree.wsgi
