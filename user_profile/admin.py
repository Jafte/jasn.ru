from django.contrib import admin
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from guardian.admin import GuardedModelAdmin


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(AuthUserAdmin, GuardedModelAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)