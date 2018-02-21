# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gofriends_site', '0004_auto_20180214_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='menuitems',
            name='short_description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='menuitems',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image'),
        ),
        migrations.DeleteModel(
            name='Properties',
        ),
    ]
