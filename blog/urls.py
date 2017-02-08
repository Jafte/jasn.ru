from django.conf.urls import url
from blog.views import BlogDetail, BlogPostDetail, BlogList, BlogUpdate, BlogCreate, BlogPostCreate, BlogPostUpdate, \
    BlogPostImageCreate

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog-list'),
    url(r'^add/$', BlogCreate.as_view(), name='blog-create'),
    url(r'^(?P<blog_slug>[\w-]+)/post-create/$', BlogPostCreate.as_view(), name='blog-post-create'),
    url(r'^(?P<blog_slug>[\w-]+)/update/$', BlogUpdate.as_view(), name='blog-update'),
    url(r'^(?P<blog_slug>[\w-]+)/p(?P<post_pk>[0-9]+)/$', BlogPostDetail.as_view(), name='blog-post-detail'),
    url(r'^(?P<blog_slug>[\w-]+)/p(?P<post_pk>[0-9]+)/update/$', BlogPostUpdate.as_view(), name='blog-post-update'),
    url(r'^(?P<blog_slug>[\w-]+)/$', BlogDetail.as_view(), name='blog-detail'),

    url(r'^img/add/$', BlogPostImageCreate.as_view(), name='image-create'),
]