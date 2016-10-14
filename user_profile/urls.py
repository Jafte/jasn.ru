from django.conf.urls import url
from user_profile.views import UserDetail, UserList, UserEdit, UserStatusEdit, UserSettingsPage

urlpatterns = [
    url(r'^edit/$', UserEdit.as_view(), name="user-profile-edit"),
    url(r'^status/$', UserStatusEdit.as_view(), name="user-profile-status-edit"),
    url(r'^settings/$', UserSettingsPage.as_view(), name="user-settings"),
    url(r'^(?P<username>[\w-]+)/$', UserDetail.as_view(), name="user-profile-detail"),
    url(r'^$', UserList.as_view(), name="user-profile-list"),
]