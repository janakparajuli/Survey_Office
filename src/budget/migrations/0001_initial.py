# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.CharField(max_length=120, verbose_name='Budget Name')),
            ],
        ),
    ]
