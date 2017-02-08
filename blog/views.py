from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from .models import Blog, Post, PostImage
from guardian.mixins import PermissionRequiredMixin
import markdown


class BlogList(ListView):
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_list.html'


class BlogDetail(DetailView):
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    queryset = Blog.objects.filter(active=True)
    template_name = 'blog/blog_detail.html'


class BlogCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'blog.add_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ['title', 'slug', 'photo', 'background', 'description']

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        form.instance.description_html = markdown.markdown(form.instance.description)
        return super(BlogCreate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'blog.change_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    fields = ['title', 'photo', 'background', 'description']
    context_object_name = 'blog'

    def form_valid(self, form):
        form.instance.description_html = markdown.markdown(form.instance.description)
        return super(BlogUpdate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class BlogPostDetail(DetailView):
    pk_url_kwarg = 'post_pk'
    queryset = Post.objects.filter(active=True)
    blog = None
    template_name = 'blog/blog_post_detail.html'

    def get_blog(self):
        if not self.blog:
            self.blog = get_object_or_404(Blog, slug=self.kwargs.get('blog_slug', False))
        return self.blog

    def get_queryset(self):
        qs = super(BlogPostDetail, self).get_queryset()
        blog = self.get_blog()
        return qs.filter(blog=blog)


class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'blog.write_post'
    template_name = 'blog/blog_post_form.html'
    model = Post
    fields = ['title', 'body', 'published', 'status']
    blog = None

    def get_permission_object(self):
        return self.get_blog()

    def get_blog(self):
        if not self.blog:
            self.blog = get_object_or_404(Blog, slug=self.kwargs.get('blog_slug', False))
        return self.blog

    def get_context_data(self, **kwargs):
        context = super(BlogPostCreate, self).get_context_data(**kwargs)
        context["blog"] = self.get_blog()

        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.body_html = markdown.markdown(form.instance.body)
        form.instance.author = user
        form.instance.blog = self.get_blog()
        return super(BlogPostCreate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class BlogPostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'post.change_post'
    template_name = 'blog/blog_post_form.html'
    model = Post
    fields = ['title', 'body', 'published', 'status']
    blog = None

    def get_blog(self):
        if not self.blog:
            self.blog = get_object_or_404(Blog, slug=self.kwargs.get('blog_slug', False))
        return self.blog

    def get_context_data(self, **kwargs):
        context = super(BlogPostUpdate, self).get_context_data(**kwargs)
        context["blog"] = self.get_blog()

        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.body_html = markdown.markdown(form.instance.body)
        form.instance.author = user
        form.instance.blog = self.get_blog()
        return super(BlogPostUpdate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()