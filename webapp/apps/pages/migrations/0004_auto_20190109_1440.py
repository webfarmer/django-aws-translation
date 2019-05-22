# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-09 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20181129_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babytimestranslation',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'es', 'Spanish'), (b'tr', 'Turkish'), (b'de', 'German'), (b'fr', 'French'), (b'ja', 'Japanese')], max_length=15, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='blogarticletranslation',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'es', 'Spanish'), (b'tr', 'Turkish'), (b'de', 'German'), (b'fr', 'French'), (b'ja', 'Japanese')], max_length=15, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='certificationtranslation',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'es', 'Spanish'), (b'tr', 'Turkish'), (b'de', 'German'), (b'fr', 'French'), (b'ja', 'Japanese')], max_length=15, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'es', 'Spanish'), (b'tr', 'Turkish'), (b'de', 'German'), (b'fr', 'French'), (b'ja', 'Japanese')], max_length=15, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='troubleshootingtranslation',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'es', 'Spanish'), (b'tr', 'Turkish'), (b'de', 'German'), (b'fr', 'French'), (b'ja', 'Japanese')], max_length=15, verbose_name='language'),
        ),
    ]