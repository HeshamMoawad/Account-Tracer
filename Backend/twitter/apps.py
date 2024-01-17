from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class TwitterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitter'
    def ready(self) -> None:
        from .workers.tasks import (
            collectorPeriodicTask ,
            accountCheckerPeriodicTask ,
            )
        scheduler = BackgroundScheduler() # ( seconds - minutes - hours )
        scheduler.add_job(collectorPeriodicTask, 'interval', minutes = 3  )  
        scheduler.add_job(accountCheckerPeriodicTask, 'interval', minutes = 6 )  
        scheduler.start()
        from .signals import (
            addAccountLoginInfoBeforeSaveTwitterAccount ,
            )
        return super().ready()