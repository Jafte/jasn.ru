# Generated by Django 3.1.3 on 2020-11-09 01:26

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import uuid_upload_path.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='slug')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_html', models.TextField(blank=True, verbose_name='description html')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=uuid_upload_path.storage.upload_to)),
                ('background', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=uuid_upload_path.storage.upload_to)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'permissions': (('write_post', 'Write post'),),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('body_html', models.TextField(verbose_name='body html')),
                ('preview', models.TextField(default='', verbose_name='preview')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Public')], default=2, verbose_name='status')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('published', models.DateTimeField(default=datetime.datetime.now, verbose_name='published')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.blog')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ('-published',),
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=uuid_upload_path.storage.upload_to)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post')),
            ],
        ),
    ]
