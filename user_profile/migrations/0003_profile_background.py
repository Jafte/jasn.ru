# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 18:01
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='backgrounds'),
        ),
    ]
