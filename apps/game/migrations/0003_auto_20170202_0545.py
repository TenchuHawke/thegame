# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20170202_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='consumeable',
            new_name='consumable',
        ),
    ]
