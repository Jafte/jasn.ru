# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import uuid_upload_path.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20161024_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Text'), (2, 'Quotation'), (3, 'Link'), (4, 'Video'), (5, 'Single Image'), (6, 'Gallery Image')], default=1, verbose_name='type')),
                ('text', models.TextField(verbose_name='data')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='description')),
                ('order', models.IntegerField(default=100, verbose_name='order')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=uuid_upload_path.storage.upload_to)),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('block', models.ManyToManyField(blank=True, null=True, related_name='images', to='blog.PostBlock')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Post')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
