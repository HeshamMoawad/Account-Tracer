from ..core.session import TwitterSession
from ..core.utils import sendTMessage
from .checker import CheckTwitterAccount , CheckAccountLoginInfo 
from ..models import (
    AccountLoginInfo ,
    TwitterAccount
)
from datetime import datetime , timedelta
import random , string

def accountCheckerPeriodicTask():
    id = ''.join(random.choices(string.ascii_letters+string.digits, k=15))
    print("\n\n[+]\tAccount Checker Periodic Task\n\n")
    sendTMessage(f"""
Start Checker Periodic Task with ID : \n{id}
    """,
    isDeveloper=True)

    accounts = TwitterAccount.objects.all()
    for account in accounts :
        CheckTwitterAccount(account)
    print("\n\n[-]\tEnd Account Checker Periodic Task\n\n")
    sendTMessage(f"""
End Checker Periodic Task with ID {id}
    """,
    isDeveloper=True)


def collectorPeriodicTask():
    id = ''.join(random.choices(string.ascii_letters+string.digits, k=15))
    print(f"\n\nCollectorPeriodicTask {id}\n\n")
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

    print(f"\n\nEnd Collector Periodic Task \n\n")
    sendTMessage(f"""
End Collector Periodic Task with ID {id}
    """,
    isDeveloper=True
    )

