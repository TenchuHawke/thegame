# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170202_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='peek_description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]