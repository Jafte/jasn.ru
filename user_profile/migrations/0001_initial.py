# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 01:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', timezone_field.fields.TimeZoneField(default='UTC')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('about', models.TextField(blank=True, verbose_name='about me')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]