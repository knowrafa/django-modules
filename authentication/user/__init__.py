from django.apps import AppConfig

default_app_config = 'authentication.user.UserConfig'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication.user'
