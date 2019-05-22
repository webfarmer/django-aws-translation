# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-01 12:30
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0048_auto_20190301_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='image',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/home/centos/sites/connect.snuza.com/webapp/media'), upload_to=pages.models.get_blog_image_path),
        ),
    ]
