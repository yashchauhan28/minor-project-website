# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectiondetail',
            name='uniqueid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.UserInformation'),
        ),
    ]
