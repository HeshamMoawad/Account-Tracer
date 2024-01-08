from ..core.userModel import User
from ..core.utils import CookiesParser
from ..core.session import TwitterSession
from ..models import TwitterAccount , AccountLoginInfo
from .TWlogin import LoginUsingBrowser
from threading import Thread 


class GetAccountLoginInfoFromInstanceThread(Thread):
    
    def __init__(self, model:TwitterAccount) -> None:
        super(GetAccountLoginInfoFromInstanceThread,self).__init__()
        self.handle = model.handle
        self.password = model.password
        self.instance = model

    def run(self) -> None:
        try :
            browser = LoginUsingBrowser()
            response = browser.login(self.handle,self.password)
            if isinstance(response , dict):
                user_data = self.createSession(response['cookie'])
                if user_data:
                    self.accountLoginInfoHandler(response['cookie'],**user_data)
        except Exception as e :
            print(e)

    def createSession(self,cookie:str):
        session = TwitterSession(cookie)
        me = session.getMe()
        user_data = me["data"]["users"]
        if user_data :
            user_data = user_data[0]["result"]
            return user_data
        else :
            return None


    def createAccountLoginInfo(self,cookie,**user_data):
        user = User(**user_data)
        new_login_info = AccountLoginInfo.objects.create(
            account = self.instance ,
            cookies = cookie ,
            token = CookiesParser(cookie).token,
            **user.params_new_instance
        )
        new_login_info.save()
        print("\nSaved\n")
        return new_login_info

    def accountLoginInfoHandler(self,cookie,**user_data):
        user = User(**user_data)
        try :
            login_info = AccountLoginInfo.objects.get(
                screen_name = self.handle.replace("@","")
            )
            login_info.name = user['name']
            login_info.profileImgURL = user['profileImgURL']
            login_info.description = user['description']
            login_info.verified = user['verified']
            login_info.save()        
            print("\nSaved\n")
            return login_info
        except AccountLoginInfo.DoesNotExist:
            return self.createAccountLoginInfo(cookie,**user_data)

