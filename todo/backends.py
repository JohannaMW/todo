from django.core.mail.backends.base import BaseEmailBackend
from todo_list.tasks import send_notify_mail

class CeleryEmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages, **kwargs):
        for msg in email_messages:
            send_notify_mail.delay(msg, **kwargs)