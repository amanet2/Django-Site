# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170507_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='create_date',
            field=models.DateTimeField(verbose_name='published on'),
        ),
    ]
