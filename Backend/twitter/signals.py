from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import TwitterAccount
from .TWlogin import LoginUsingBrowser
from threading import Thread , currentThread
from .core.session import TwitterSession
from easydict import EasyDict


def threadedFuncLogin(sender:TwitterAccount):
    # try :
        browser = LoginUsingBrowser()
        result = browser.login(sender.handle , sender.password , logging_with_print=True)
        print(result)
        # if isinstance(result , dict):
        #     session = TwitterSession(result.get("cookie"))
        #     accountResponse = session.getMe()
        #     print(accountResponse)
    # except Exception as e :
    #     print(f"\nError in Thread {currentThread().name} - {e}\n")



@receiver(pre_save,sender=TwitterAccount)
def addAccountLoginInfoBeforeSaveTwitterAccount(sender:TwitterAccount , **kwargs):
    print(f"\npre_save will threaded {sender}\n")
    # task = Thread(target=threadedFuncLogin,args=(sender,))
    # task.start()
    threadedFuncLogin(sender)
    print(f"\npre_save end with task name = {sender}\n")
    
