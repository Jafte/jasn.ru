from django.conf.urls import url
from user_profile.views import UserDetail, UserList, UserEdit, UserSettingsPage, UserBlogList

urlpatterns = [
    url(r'^edit/$', UserEdit.as_view(), name="user-profile-edit"),
    url(r'^settings/$', UserSettingsPage.as_view(), name="user-settings"),
    url(r'^blogs/$', UserBlogList.as_view(), name="user-blogs"),
    url(r'^(?P<username>[\w-]+)/$', UserDetail.as_view(), name="user-profile-detail"),
    url(r'^$', UserList.as_view(), name="user-profile-list"),
]