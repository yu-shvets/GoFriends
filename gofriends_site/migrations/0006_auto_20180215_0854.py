# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gofriends_site', '0005_auto_20180215_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.RenameModel(
            old_name='MenuItems',
            new_name='Items',
        ),
        migrations.AddField(
            model_name='images',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gofriends_site.Items'),
        ),
    ]