from django.apps import AppConfig

default_app_config = 'authentication.permissions.PermissionsConfig'


class PermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication.permissions'
