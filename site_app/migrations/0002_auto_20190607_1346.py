# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-07 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteholdings',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_holdings', to='site_app.Site'),
        ),
    ]
