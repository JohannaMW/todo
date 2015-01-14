from django.conf import settings
from django.core.mail import get_connection
from django.utils.timezone import utc
from models import Task
from celery.task import Task
from todo.celery import app
import models
import datetime
from django.core import mail

@app.task(name='send_due_mail')
def send_due_mail():
    tasks = models.Task.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc,second=00, microsecond=00)
    for task in tasks:
        if task.due == now and task.notified == False:
            mail.send_mail('{} is due!'.format(task.title),
                     'Hey {}, your task {} is due! Description: {}'.format(task.owner.first_name, task.title, task.description),
                     'from@example.com', ['{}'.format(task.owner.email)])
            task.notified == True