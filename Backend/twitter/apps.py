from django.apps import AppConfig


class TwitterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitter'

    def ready(self) -> None:
        from .signals import (
            addAccountLoginInfoBeforeSaveTwitterAccount ,
            )
        return super().ready()