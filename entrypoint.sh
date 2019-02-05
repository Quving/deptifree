#!/bin/bash
set -e
python manage.py collectstatic
gunicorn -c gunicorn_conf.py deptifree.wsgi
