from django.apps import AppConfig


class UserinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userInfo'

    def ready(self):
        import userInfo.signals