from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TwitterAccount 
from .threads import GetAccountLoginInfoFromInstanceThread


@receiver(post_save,sender=TwitterAccount)
def addAccountLoginInfoBeforeSaveTwitterAccount( sender:TwitterAccount , instance :TwitterAccount, **kwargs):
    print(f"\n post_save will threaded {instance}\n")
    GetAccountLoginInfoFromInstanceThread(instance).start()
    print(f"\n post_save end with task name = {instance}\n")
    

