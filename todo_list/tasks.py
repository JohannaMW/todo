from django.conf import settings
from django.core.mail import get_connection
from django.utils.timezone import utc
from todo.celery import app
import models
import datetime
from django.core import mail
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

BACKEND = getattr(settings, 'CELERY_EMAIL_BACKEND',
                  'django.core.mail.backends.smtp.EmailBackend')

@app.task(name='send_due_mail')
def send_due_mail():
    tasks = models.Task.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc,second=00, microsecond=00)
    conn = get_connection(backend=BACKEND)
    for task in tasks:
        if task.due == now and task.notified is False:
            conn.send_message('{} is due!'.format(task.title),
                     'Hey {}, your task {} is due! Description: {}'.format(task.owner.first_name, task.title, task.description),
                     'from@example.com', ['{}'.format(task.owner.email)])
            task.notified = True
        else:
            pass

@app.task(name='send_notify_mail')
def send_notify_mail(message, **kwargs):
    conn = get_connection(backend=BACKEND)
    try:
        result = conn.send_messages([message])
        logger.debug("Message successfully sent")
        return result
    except Exception as e:
        logger.warning("Failed to deliver message")
        send_notify_mail.retry(exc=e)


