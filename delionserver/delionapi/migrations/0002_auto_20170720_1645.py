# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delionapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='delionapi.Shop', to_field='shop_name'),
        ),
    ]
