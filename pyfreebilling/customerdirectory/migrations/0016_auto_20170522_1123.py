# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-22 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerdirectory', '0015_auto_20170117_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdirectory',
            name='insee_code',
            field=models.CharField(blank=True, help_text='Postal code, INSEE code ... for routing\n          urgency number to the right urgency call center.', max_length=10, null=True, verbose_name='Special code for routing urgency numbers'),
        ),
    ]