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
        scheduler.add_job(collectorPeriodicTask, 'interval', minutes = 55 )  
        scheduler.add_job(accountCheckerPeriodicTask, 'cron', hour = 0 )  
        scheduler.add_job(accountCheckerPeriodicTask, 'cron', hour = 6  )  
        scheduler.add_job(accountCheckerPeriodicTask, 'cron', hour = 12 )  
        scheduler.add_job(accountCheckerPeriodicTask, 'cron', hour = 18 )  
        scheduler.add_job(accountCheckerPeriodicTask, 'cron', hour = 22 )  
        if not scheduler.running :
            print("Not Running")
            scheduler.start()
        from .signals import (
            addAccountLoginInfoBeforeSaveTwitterAccount ,
            )
        return super().ready()