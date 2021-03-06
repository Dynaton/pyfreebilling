# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-29 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('did', '0004_auto_20161029_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='did',
            name='cust_max_channels',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='maximum simultaneous calls allowed\n            for this did. 0 means no limit', null=True, verbose_name='customer channels'),
        ),
        migrations.AlterField(
            model_name='did',
            name='prov_max_channels',
            field=models.PositiveIntegerField(default=0, help_text='maximum simultaneous calls allowed\n            for this did. 0 means no limit', verbose_name='provider channels'),
        ),
    ]
