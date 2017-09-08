# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0002_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='short_description',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
