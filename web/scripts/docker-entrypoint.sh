#!/bin/sh
python manage.py makemigrations && /
python manage.py migrate && /
python manage.py collectstatic --noinput --clear && /
gunicorn blog.wsgi:application --bind :8000 --timeout 1800 --workers 4 --reload