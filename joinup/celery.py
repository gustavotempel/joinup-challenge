import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joinup.settings')

app = Celery('joinup')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()