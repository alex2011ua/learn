# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
