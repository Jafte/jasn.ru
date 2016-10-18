from django.conf.urls import url
from user_profile.views import UserDetail, UserList, UserEdit, UserSettingsPage, UserBlogList, \
    BlogCreate

urlpatterns = [
    url(r'^edit/$', UserEdit.as_view(), name="user-profile-edit"),
    url(r'^settings/$', UserSettingsPage.as_view(), name="user-settings"),
    url(r'^blog/new/$', BlogCreate.as_view(), name="user-blog-create"),
    url(r'^blog/$', UserBlogList.as_view(), name="user-blog-list"),
    url(r'^(?P<username>[\w-]+)/$', UserDetail.as_view(), name="user-profile-detail"),
    url(r'^$', UserList.as_view(), name="user-profile-list"),
]