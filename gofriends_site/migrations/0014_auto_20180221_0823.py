# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 08:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gofriends_site', '0013_auto_20180219_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('url_field', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Case Study',
                'ordering': ['-created'],
                'verbose_name_plural': 'Case Studies',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Industry',
                'ordering': ['-created'],
                'verbose_name_plural': 'Industries',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Service',
                'ordering': ['-created'],
                'verbose_name_plural': 'Services',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Technology',
                'ordering': ['-created'],
                'verbose_name_plural': 'Technologies',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='item',
        ),
        migrations.RemoveField(
            model_name='items',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='items',
            name='section',
        ),
        migrations.AlterField(
            model_name='customers',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Sections',
        ),
    ]