# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenebuilder', '0002_auto_20170515_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='map_path',
            field=models.CharField(default='1.map', max_length=32),
            preserve_default=False,
        ),
    ]
