import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated():
            if hasattr(request.user, 'profile'):
                user_timezone = request.user.profile.timezone
                if user_timezone:
                    timezone.activate(user_timezone)
                else:
                    timezone.deactivate()