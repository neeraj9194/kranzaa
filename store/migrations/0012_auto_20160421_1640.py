# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20160418_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regstore',
            name='category',
        ),
        migrations.AddField(
            model_name='regstore',
            name='category',
            field=models.ManyToManyField(default=None, to='store.Category'),
        ),
    ]