# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-30 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20190123_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='display',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
