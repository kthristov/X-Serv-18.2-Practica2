# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 01:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20160419_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls_list',
            old_name='url',
            new_name='url_entry',
        ),
    ]