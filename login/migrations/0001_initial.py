# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 17:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_name', models.CharField(max_length=30)),
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
    ]
