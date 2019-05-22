# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-06 10:24
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_auto_20190206_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='image',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/root/sites/connect.snuza.com/webapp/media'), upload_to=pages.models.get_blog_image_path),
        ),
    ]
