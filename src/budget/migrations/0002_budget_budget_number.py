# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='budget_number',
            field=models.CharField(default=21111, max_length=120, verbose_name='Budget Number'),
            preserve_default=False,
        ),
    ]