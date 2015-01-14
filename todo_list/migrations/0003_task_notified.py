# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20150114_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
