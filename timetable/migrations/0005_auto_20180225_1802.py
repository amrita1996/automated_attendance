# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='hour1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Subject'),
        ),
    ]