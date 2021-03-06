# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_display', '0002_auto_20160415_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='camera',
            name='productId',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='productId',
            field=models.CharField(max_length=110),
        ),
    ]
