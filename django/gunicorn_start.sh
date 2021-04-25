#!/bin/sh

echo "...Starting Django Application"

python3 manage.py collectstatic  --noinput
gunicorn --workers=1 --bind=0.0.0.0:8000 project_name.wsgi:application  --threads=2 --worker-connections=500 --log-level=debug --timeout=120
