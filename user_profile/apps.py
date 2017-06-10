from django.apps import AppConfig, apps


# class UserProfileConfig(AppConfig):
#     name = 'user_profile'
#
#     def ready(self):
#         from actstream import registry
#         registry.register(apps.get_model('auth.user'))