# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20160426_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='ratings',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]