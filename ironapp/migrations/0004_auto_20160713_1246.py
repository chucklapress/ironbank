# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ironapp', '0003_auto_20160713_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acctbalance',
            name='entry',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
