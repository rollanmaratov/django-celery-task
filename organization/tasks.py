from __future__ import absolute_import, unicode_literals

from somnium.celery import app
from .service import send

@app.task
def send_notification(user_email, name, task_description):
    send(user_email, name, task_description)

