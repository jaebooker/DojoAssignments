# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20170217_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='comment',
        ),
    ]