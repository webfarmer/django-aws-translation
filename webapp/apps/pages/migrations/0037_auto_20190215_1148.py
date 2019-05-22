# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-15 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_auto_20190215_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='babytimes',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certification',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='troubleshooting',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]