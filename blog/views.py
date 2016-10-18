from django.views.generic import ListView, DetailView
from blog.models import Blog, Post


class BlogDetail(DetailView):
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_detail.html'


class BlogPostDetail(DetailView):
    pk_url_kwarg = 'post_pk'
    queryset = Post.objects.filter(active=True, status=2)
    template_name = 'blog/blog_post_detail.html'


class BlogList(ListView):
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_list.html'
