# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '0003_auto_20160329_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelabels',
            name='labelShapes',
            field=models.TextField(max_length=10000),
        ),
    ]