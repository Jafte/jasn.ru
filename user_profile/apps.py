from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('User'))