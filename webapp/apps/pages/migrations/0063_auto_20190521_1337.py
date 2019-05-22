# Generated by Django 2.2.1 on 2019-05-21 11:37

import django.core.files.storage
from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0062_auto_20190430_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='image',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/', location='/Users/king/development/connect.snuza.com/webapp/media'), upload_to=pages.models.get_blog_image_path),
        ),
    ]
