# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ironapp', '0006_auto_20160713_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='from_account',
        ),
        migrations.AddField(
            model_name='acctbalance',
            name='transfer_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
    ]