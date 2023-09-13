#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic
if [ "$ENVIRONMENT" != "production" ]; then
    echo "Iniciando servidor de desenvolvimento..."
    uwsgi --ini uwsgi/uwsgi.dev.ini
else
    echo "Iniciando servidor de produção..."
    uwsgi --ini uwsgi/uwsgi.prod.ini
fi