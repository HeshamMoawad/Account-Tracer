import requests , datetime
from ..models import TelegramBotUser
from .constants import TELEGRAM_BOT_URL , TELEGRAM_BOT_DEV_URL
import threading


def __sendTMessage(user_id:int,msg):
    try :
        params = {
            'chat_id': user_id ,
            'text': f"{datetime.datetime.now().strftime('%Y-%m-%d & %H:%M:%S')}\n{msg}" ,
        }
        resp = requests.get(TELEGRAM_BOT_URL,params=params)
    except Exception as e :
        print (f"[-]\tError in __sendTMessage: {e}")

def __sendTMessageDev(msg):
    try :
        params = {
            'chat_id': 1077637654 ,
            'text': f"{datetime.datetime.now().strftime('%Y-%m-%d & %H:%M:%S')}\n{msg}" ,
        }
        requests.get(TELEGRAM_BOT_DEV_URL,params=params)

    except Exception as e :
        print (f"[-]\tError in __sendTMessageDev: {e}")

def sendTMessage(msg:str,isDeveloper:bool=False):
    if not isDeveloper:
        ids = TelegramBotUser.objects.all()
        for user_id in ids :
            __sendTMessage(user_id.telegram_user_id,msg)
    else :
        __sendTMessageDev(msg)
 

