# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20160908_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer4',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.TextField(default='/static/BaconSpaceKitty.jpg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_image',
            field=models.TextField(default='/static/BaconSpaceKitty.jpg'),
            preserve_default=False,
        ),
    ]
