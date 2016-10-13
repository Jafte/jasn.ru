from django.utils.deprecation import MiddlewareMixin
from last_seen.models import user_seen

class LastSeenMiddleware(MiddlewareMixin):
   def process_request(self, request):
        if request.user.is_authenticated():
            user_seen(request.user)