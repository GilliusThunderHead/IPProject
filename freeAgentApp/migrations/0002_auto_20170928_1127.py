# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeAgentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='project',
            name='file_type',
            field=models.FileField(upload_to=''),
        ),
    ]
