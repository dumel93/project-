# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type_page', '0003_auto_20170711_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballtype',
            name='course',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
