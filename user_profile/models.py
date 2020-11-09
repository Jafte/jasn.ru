from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

from timezone_field import TimeZoneField
from easy_thumbnails.fields import ThumbnailerImageField
from uuid_upload_path import upload_to
from guardian.shortcuts import assign_perm

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )

    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='profile', on_delete=models.CASCADE)
    timezone = TimeZoneField(default='UTC')
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    photo = ThumbnailerImageField(upload_to=upload_to, blank=True)
    background = ThumbnailerImageField(upload_to=upload_to, blank=True)
    status = models.CharField(_('status'), blank=True, max_length=100)
    about = models.TextField(_('about me'), blank=True)
    followers_counter = models.PositiveIntegerField(_('followers counter'), default=0)
    subscriptions_counter = models.PositiveIntegerField(_('subscriptions counter'), default=0)
    blogs_counter = models.PositiveIntegerField(_('blogs counter'), default=0)
    clubs_counter = models.PositiveIntegerField(_('clubs counter'), default=0)

    def last_seen(self):
        return False

    def is_online(self):
        return False

    def get_absolute_url(self):
        return reverse('user-profile-detail', kwargs={'username': self.user.username})

    def get_active_blogs(self):
        return self.user.blogs.all().filter(active=True)

    def __str__(self):
        return '%s profile' % self.user

@receiver(post_save, sender=User)
def user_changed(sender, **kwargs):
    user, created = kwargs["instance"], kwargs["created"]
    if created and user.username != settings.ANONYMOUS_USER_NAME:
        profile = Profile(user=user)
        profile.save()
        assign_perm("change_user", user, user)
        assign_perm("change_profile", user, profile)

post_save.connect(user_changed, sender=User)