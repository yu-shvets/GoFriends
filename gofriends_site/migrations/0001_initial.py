# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='gofriends_site.MenuItems', verbose_name='parent сategory')),
            ],
            options={
                'verbose_name_plural': 'Menu items',
                'abstract': False,
                'verbose_name': 'Menu item',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Sections',
                'abstract': False,
                'verbose_name': 'Section',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='menuitems',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gofriends_site.Sections'),
        ),
    ]
