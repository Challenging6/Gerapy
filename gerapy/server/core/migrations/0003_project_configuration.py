# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_monitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='configuration',
            field=models.TextField(blank=True, default=''),
        ),
    ]
