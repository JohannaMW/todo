from django.core.mail.backends.base import BaseEmailBackend
from .tasks import SendEmailTask

class CeleryEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        SendEmailTask.apply_async(args=[email_messages], queue='emails')