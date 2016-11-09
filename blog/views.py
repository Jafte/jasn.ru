from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Blog, Post
from guardian.mixins import PermissionRequiredMixin
import markdown


class BlogDetail(DetailView):
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_detail.html'


class BlogPostDetail(DetailView):
    pk_url_kwarg = 'post_pk'
    queryset = Post.objects.filter(active=True, status=2)
    template_name = 'blog/blog_post_detail.html'


class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'blog.write_post'
    template_name = 'blog/post_form.html'
    model = Post
    blog = None
    fields = ['title', 'status', 'body', 'published']

    def get_permission_object(self):
        return self.blog

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, slug=kwargs.get('blog_slug', False))
        return super(BlogPostCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        user = self.request.user
        form.instance.author = user
        form.instance.blog = self.blog
        form.instance.body_html = markdown.markdown(self.body)
        return super(BlogPostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-post-detail', kwargs={'blog_slug': self.object.blog.slug, 'post_pk': self.object.pk})


class BlogPostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'blog.change_post'
    template_name = 'blog/post_form.html'
    model = Post
    pk_url_kwarg = 'post_pk'
    fields = ['title', 'status', 'body', 'published']

    def form_valid(self, form):
        form.instance.body_html = markdown.markdown(form.instance.body)
        return super(BlogPostUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-post-detail', kwargs={'blog_slug': self.object.blog.slug, 'post_pk': self.object.pk})


class BlogList(ListView):
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_list.html'


class BlogCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'blog.add_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ['title', 'slug', 'photo', 'description']

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        form.instance.description_html = markdown.markdown(form.instance.description)
        return super(BlogCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'blog_slug': self.object.slug})


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'blog.change_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    fields = ['title', 'photo', 'description']
    context_object_name = 'blog'

    def form_valid(self, form):
        form.instance.description_html = markdown.markdown(form.instance.description)
        return super(BlogUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'blog_slug': self.object.slug})