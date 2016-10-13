# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 00:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastSeen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(default='default', max_length=20)),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-last_seen',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='lastseen',
            unique_together=set([('user', 'site', 'module')]),
        ),
    ]
