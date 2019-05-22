# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-15 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0035_auto_20190215_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailChimpList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='babytimes',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('live', 'Live / Published')], default='draft', max_length=34),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('live', 'Live / Published')], default='draft', max_length=34),
        ),
        migrations.AddField(
            model_name='certification',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('live', 'Live / Published')], default='draft', max_length=34),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('live', 'Live / Published')], default='draft', max_length=34),
        ),
        migrations.AddField(
            model_name='troubleshooting',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('live', 'Live / Published')], default='draft', max_length=34),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='mailchimp_list',
            field=models.ManyToManyField(blank=True, to='pages.MailChimpList'),
        ),
    ]
