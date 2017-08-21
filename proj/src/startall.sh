#!/bin/bash

cd /root/Documents/GITHUB/WeatherStation/proj/
source bin/activate
cd src

echo `pwd`

service rabbitmq-server start
python manage.py runserver &
celery -A proj worker -l info -S django &
celery -A proj beat -l info -S django &
flower -A proj --port=5555 &

