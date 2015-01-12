from django.conf import settings
from django.core.mail import get_connection

from celery.task import Task

BACKEND = getattr(settings, 'CELERY_EMAIL_BACKEND',
                  'django.core.mail.backends.smtp.EmailBackend')
class SendEmailTask(Task):
    def run(self, email_messages, **kwargs):
        conn = get_connection(backend=BACKEND)
        conn.send_messages(email_messages)
