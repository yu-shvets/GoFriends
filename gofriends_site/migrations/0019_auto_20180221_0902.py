# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gofriends_site', '0018_auto_20180221_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
