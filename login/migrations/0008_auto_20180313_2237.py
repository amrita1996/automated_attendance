# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_staff_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Subject'),
        ),
    ]