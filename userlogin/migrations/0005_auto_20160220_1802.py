# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 18:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_auto_20160219_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguser',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone no.', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]