# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20180227_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='hour',
            field=models.IntegerField(default=0),
        ),
    ]