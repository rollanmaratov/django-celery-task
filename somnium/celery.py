from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from somnium import settings
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'somnium.settings')

app = Celery('somnium')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
