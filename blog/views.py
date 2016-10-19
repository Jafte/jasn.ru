from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse
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


class BlogCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ['title', 'slug', 'description']

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(BlogCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'blog_slug': self.object.slug})


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    permission_required = 'blog.edit_blog'
    template_name = 'blog/blog_form.html'
    model = Blog
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    fields = ['title', 'description']
    context_object_name = 'blog'

    def test_func(self):
        blog = self.get_object()
        return blog.owner == self.request.user

    def form_valid(self, form):
        return super(BlogUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'blog_slug': self.object.slug})