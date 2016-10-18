from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.forms import UserForm
from django.urls import reverse
from actstream import action


class UserDetail(DetailView):
    slug_field = 'username'
    context_object_name = "user_data"
    slug_url_kwarg = 'username'
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_detail.html'


class UserList(ListView):
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_list.html'


class UserSettingsPage(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile/user_settings.html'


class UserEdit(LoginRequiredMixin, FormView):
    template_name = 'user_profile/user_edit.html'
    form_class = UserForm

    def get_initial(self):
        user = self.request.user
        initial = super(UserEdit, self).get_initial()
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['status'] = user.profile.status
        initial['timezone'] = user.profile.timezone
        initial['gender'] = user.profile.gender
        initial['birth_date'] = user.profile.birth_date
        initial['about'] = user.profile.about
        initial['photo'] = user.profile.photo
        initial['background'] = user.profile.background

        return initial

    def form_valid(self, form):
        user = self.request.user

        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        user.profile.status = form.cleaned_data['status']
        user.profile.timezone = form.cleaned_data['timezone']
        user.profile.gender = form.cleaned_data['gender']
        user.profile.birth_date = form.cleaned_data['birth_date']
        user.profile.about = form.cleaned_data['about']
        user.profile.photo = form.cleaned_data['photo']
        user.profile.background = form.cleaned_data['background']
        user.profile.save()

        return super(UserEdit, self).form_valid(form)

    def get_success_url(self):
        return reverse('user-profile-detail', kwargs={'username': self.request.user.username})