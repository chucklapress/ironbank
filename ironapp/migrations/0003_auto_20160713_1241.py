# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ironapp', '0002_auto_20160713_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acctbalance',
            name='entry',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]
