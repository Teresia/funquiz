# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='slug',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
