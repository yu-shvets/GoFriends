# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gofriends_site', '0019_auto_20180221_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='services/icons'),
        ),
        migrations.AlterField(
            model_name='casestudies',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='case_studies', verbose_name='title image'),
        ),
        migrations.AlterField(
            model_name='industries',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='industries/images', verbose_name='title image'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='services/images', verbose_name='title image'),
        ),
        migrations.AlterField(
            model_name='technologies',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='technologies/images', verbose_name='title image'),
        ),
    ]
