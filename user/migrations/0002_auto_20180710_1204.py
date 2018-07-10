# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-10 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='platform_icon',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='platform_id',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
