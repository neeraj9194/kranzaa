# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_comments_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='created',
        ),
    ]