#!/bin/bash
python manage.py migrate # Run migrations
python manage.py collectstatic --noinput  # collect static files
gunicorn cartloop.wsgi:application --bind 0.0.0.0:8000 # run application using gunicorn
