from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

import datetime

@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    active = models.BooleanField(_('active'), default=True)
    description = models.TextField(_('description'), blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __str__(self):
        return '%s by %s' % (self.title, self.owner)

    def get_absolute_url(self):
        return ('blog-detail', None, {'blog_slug': self.slug,})

@python_2_unicode_compatible
class Post(models.Model):
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, related_name='posts')
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    active = models.BooleanField(_('active'), default=True)
    published = models.DateTimeField(_('published'), default=datetime.datetime.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering  = ('-published',)
        get_latest_by = 'published'

    def __str__(self):
        return '%s in blog %s' % (self.title, self.blog)

    def get_absolute_url(self):
        return ('blog-post-detail', None, {'blog_slug': self.blog.slug, 'post_pk': self.pk})