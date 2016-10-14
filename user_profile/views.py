from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

class UserDetail(DetailView):
    slug_field = 'username'
    context_object_name = "user_data"
    slug_url_kwarg = 'username'
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_detail.html'

class UserList(ListView):
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_list.html'

        