# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_comments_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
