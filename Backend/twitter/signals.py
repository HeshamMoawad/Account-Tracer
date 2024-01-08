from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TwitterAccount
from .workers.threads import GetAccountLoginInfoFromInstanceThread
from .workers.checker import CheckTwitterAccount

@receiver(post_save, sender=TwitterAccount)
def addAccountLoginInfoBeforeSaveTwitterAccount(sender: TwitterAccount, instance: TwitterAccount, **kwargs):
    # GetAccountLoginInfoFromInstanceThread(instance).start()
    checker = CheckTwitterAccount(instance)


