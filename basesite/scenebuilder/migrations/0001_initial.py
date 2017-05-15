# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=64)),
                ('map_date', models.DateTimeField(verbose_name='published on')),
                ('map_author', models.CharField(max_length=32)),
            ],
        ),
    ]
