# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ironapp', '0005_auto_20160713_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='transfer_amount',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
