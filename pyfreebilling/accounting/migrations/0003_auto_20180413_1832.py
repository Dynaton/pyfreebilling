# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_acccdr'),
    ]

    operations = [
        migrations.AddField(
            model_name='acc',
            name='time_attr',
            field=models.IntegerField(default=0, help_text='Unix timestamp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acc',
            name='time_exten',
            field=models.IntegerField(default=0, help_text='extended value related to the time of event'),
            preserve_default=False,
        ),
    ]
