from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.core.validators import MinLengthValidator
from easy_thumbnails.fields import ThumbnailerImageField
from uuid_upload_path import upload_to
from django.db.models.signals import post_save

import datetime

STATUS_CHOICES = (
    (1, _('Draft')),
    (2, _('Public')),
)

TYPE_CHOICES = (
    (1, _('Text')),
    (2, _('Quotation')),
    (3, _('Link')),
    (4, _('Video')),
    (5, _('Single Image')),
    (6, _('Gallery Image')),
)


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True, max_length=100, validators=[MinLengthValidator(4)])
    active = models.BooleanField(_('active'), default=True)
    description = models.TextField(_('description'), blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    photo = ThumbnailerImageField(upload_to=upload_to, blank=True)
    owner = models.ForeignKey(User, related_name='blogs')

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __str__(self):
        return '%s by %s' % (self.title, self.owner)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'blog_slug': self.slug})

    def get_posts(self):
        return self.posts.all().filter(blog=self, active=True, published__lte=datetime.datetime.now())


def blog_changed(sender, **kwargs):
    blog = kwargs["instance"]
    user = blog.owner
    user.profile.blogs_counter = user.profile.get_active_blogs().count()
    user.profile.save()

post_save.connect(blog_changed, sender=Blog)

@python_2_unicode_compatible
class Post(models.Model):
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
        ordering = ('-published',)
        get_latest_by = 'published'

    def __str__(self):
        return '%s in blog %s' % (self.title, self.blog)

    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'blog_slug': self.blog.slug, 'post_pk': self.pk})


@python_2_unicode_compatible
class PostBlock(models.Model):
    post = models.ForeignKey(Post, related_name='blocks')
    type = models.IntegerField(_('type'), choices=TYPE_CHOICES, default=1)
    text = models.TextField(_('data'))
    description = models.CharField(_('description'), max_length=200, blank=True)
    owner = models.ForeignKey(User, related_name='blocks')
    order = models.IntegerField(_('order'), default=100)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return 'block %s for %s' % (self.type, self.post)


@python_2_unicode_compatible
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images')
    block = models.ManyToManyField(PostBlock, related_name='images', blank=True, null=True)
    owner = models.ForeignKey(User, related_name='images')
    image = ThumbnailerImageField(upload_to=upload_to)
    description = models.CharField(_('description'), max_length=200, blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return 'image for %s' % self.post
