from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

# app = Celery('tasks', backend='rpc://', broker='pyamqp://guest:guest@localhost:8000//')
# app = Celery('muypicky', backend='rpc://', broker='pyamqp://guest:guest@localhost:8000//')
app = Celery('proj', backend='rpc://', broker='pyamqp://guest:guest@localhost:5672//')
# app = Celery('muypicky')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Bucharest',
    enable_utc=True,
)

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))