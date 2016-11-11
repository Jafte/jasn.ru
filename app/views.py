from django.views.generic import TemplateView
from blog.models import Post
import  datetime


class IndexPageList(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageList, self).get_context_data(**kwargs)
        context["post_list"] = Post.objects.filter(active=True, status=2, published__lte=datetime.datetime.now()).order_by("-published")[:20]
        return context