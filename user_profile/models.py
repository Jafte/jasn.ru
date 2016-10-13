from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from django.urls import reverse

from django.db.models.signals import post_save

class Profile(models.Model):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )

    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='profile') 
    timezone = TimeZoneField(default='UTC')
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    about = models.TextField(_('about me'), blank=True)
    
    def last_seen(self):
        return False

    def is_online(self):
        return False

    def get_absolute_url(self):
        return reverse('user_profile_detail', kwargs={'username': self.user.username,})

    def __str__(self):
        return '%s profile' % (self.user)


def user_changed(sender, **kwargs):
    user = kwargs["instance"]
    if hasattr(user, 'profile'):
        pass
    else:
        profile = Profile(user=user)
        profile.save()

post_save.connect(user_changed, sender=User)