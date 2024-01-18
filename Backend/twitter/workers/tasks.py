from ..core.session import TwitterSession
from ..core.utils import sendTMessage
from .checker import CheckTwitterAccount , CheckAccountLoginInfo 
from ..models import (
    AccountLoginInfo ,
    TwitterAccount
)
from datetime import datetime , timedelta
import random , string , logging


def accountCheckerPeriodicTask():
    # logger = logging.getLogger(__name__)
    id = ''.join(random.choices(string.ascii_letters+string.digits, k=15))
    print(f"[+]\tStart Checker Periodic Task with ID : {id}")
    sendTMessage(f"""
Start Checker Periodic Task with ID : \n{id}
    """,
    isDeveloper=True)

    accounts = TwitterAccount.objects.all()
    for account in accounts :
        CheckTwitterAccount(account)
    sendTMessage(f"""
End Checker Periodic Task with ID {id}
    """,
    isDeveloper=True)
    print(f"[-]\tEnd Checker Periodic Task with ID : {id}")


def collectorPeriodicTask():
    id = ''.join(random.choices(string.ascii_letters+string.digits, k=15))
    print(f"[+]\t Start Collector Periodic Task {id}")
    sendTMessage(f"""
Start Collector Periodic Task with ID {id}
    """,
    isDeveloper=True)
    infos = AccountLoginInfo.objects.all()
    for account in infos :
        print(f"[+]\tCollect {account}")
        session = TwitterSession(account.cookies , max_older=datetime.now()-timedelta(days=-5))
        session.saveMyStats()
        session.saveMyTweets()
        session.saveMyChats()
        print(f"[-]\tEnd Collect {account}")

    print(f"[+]\tEnd Collector Periodic Task with ID : {id} ")
    sendTMessage(f"""
End Collector Periodic Task with ID {id}
    """,
    isDeveloper=True
    )

