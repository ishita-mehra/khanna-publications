release: python manage.py migrate --noinput
web: python manage.py collectstatic --noinput && gunicorn khanna_publications.wsgi:application