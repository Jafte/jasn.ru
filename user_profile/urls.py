from django.conf.urls import url
from user_profile.views import UserDetail, UserList

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', UserDetail.as_view(), name="user-profile-detail"),
    url(r'^$', UserList.as_view(), name="user-profile-list"),
]