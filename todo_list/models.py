from django.contrib.auth.models import User
from django.db import models
import django.dispatch

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due = models.DateTimeField()
    notified = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='owner')

    def __unicode__(self):
        return u"{}".format(self.title)