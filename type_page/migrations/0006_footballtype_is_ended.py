# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type_page', '0005_footballtype_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballtype',
            name='is_ended',
            field=models.BooleanField(default=False),
        ),
    ]
