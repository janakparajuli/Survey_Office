# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_budget_budget_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_number',
            field=models.CharField(default='N/A', max_length=120, verbose_name='Budget Number'),
        ),
    ]