# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-23 10:09
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_merge_20190123_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certification',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='image',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/Users/paulvonhoesslin/development/connect.snuza.com/webapp/media'), upload_to=pages.models.get_blog_image_path),
        ),
    ]
