from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class JasnAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/user/{username}/"
        return path.format(username=request.user.username)