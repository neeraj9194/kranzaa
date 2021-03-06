# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20160421_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='ratings',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
        migrations.AlterField(
            model_name='regstore',
            name='city',
            field=models.CharField(choices=[('delhi', 'Delhi'), ('mumbai', 'Mumbai')], default='DEL', max_length=20),
        ),
        migrations.AlterField(
            model_name='regstore',
            name='main_pic',
            field=models.ImageField(upload_to='static/store_img/'),
        ),
    ]
