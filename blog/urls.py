from django.conf.urls import url
from blog.views import BlogDetail, BlogPostDetail, BlogList

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog-list'),
    url(r'^(?P<blog_slug>[\w-]+)/$', BlogDetail.as_view(), name='blog-detail'),
    url(r'^(?P<blog_slug>[\w-]+)/p(?P<pk>[0-9]+)/$', BlogPostDetail.as_view(), name='blog-post-detail'),
]