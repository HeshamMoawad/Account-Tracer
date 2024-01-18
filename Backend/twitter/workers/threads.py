from ..core.objects import UserObject
from ..core.parsers import CookiesParser
from ..core.session import TwitterSession
from ..models import TwitterAccount , AccountLoginInfo
from .TWlogin import LoginUsingBrowser
from threading import Thread 
from ..core.utils import sendTMessage
import traceback

class GetAccountLoginInfoFromInstanceThread(Thread):
    
    def __init__(self, instance:TwitterAccount) -> None:
        super(GetAccountLoginInfoFromInstanceThread,self).__init__()
        self.handle = instance.handle
        self.password = instance.password
        self.instance = instance

    def run(self) -> None:
        try :
            browser = LoginUsingBrowser()
            response = browser.login(self.handle,self.password)
            if isinstance(response , dict):
                user_data = self.createSession(response['cookie'])
                if user_data:
                    self.accountLoginInfoHandler(response['cookie'],**user_data)
                else :
                    sendTMessage(f"""
Faild Login as : {self.instance.agent} with user_data {user_data}
Username : {self.handle}
Password : {self.password}
                        """,
                        isDeveloper=True
                        )
                    sendTMessage(f"""
Faild Login as : {self.instance.agent}
Username : {self.handle}
Password : {self.password}
Please Check Handle or Password
                        """)
            else:
                sendTMessage(f"""
Faild Login as : {self.instance.agent} with Response {response}
Username : {self.handle}
Password : {self.password}
                    """,
                    isDeveloper=True
                    )
                sendTMessage(f"""
Faild Login as : {self.instance.agent}
Username : {self.handle}
Password : {self.password}
Please Check Handle or Password 
                    """)
                
        except Exception as e :
            sendTMessage(f"""
Faild Login as : {self.instance.agent}
Username : {self.handle}
Password : {self.password}
Please Check Handle or Password 
            """)
            sendTMessage(f"""
Faild Login as : {self.instance.agent}
Username : {self.handle}
Password : {self.password}
Error is {e}
            """,
            isDeveloper=True
            )

            print(e)

    def createSession(self,cookie:str):
        session = TwitterSession(cookie , only_get_me=True)
        me = session._getMe()
        if me :
            user_data = me["data"]["users"]
            if user_data :
                user_data = user_data[0]["result"]
                return user_data
            else :
                sendTMessage(f"""
Faild user_data with {user_data} 
                """,
                isDeveloper=True
                )
        else :
            sendTMessage(f"""
Faild _getMe with Response {me}
            """,
            isDeveloper=True
            )


    def createAccountLoginInfo(self,cookie,**user_data):
        user = UserObject(**user_data)
        new_login_info = AccountLoginInfo.objects.create(
            account = self.instance ,
            cookies = cookie ,
            token = CookiesParser(cookie).token,
            **user.params_new_instance
        )
        new_login_info.save()
        sendTMessage(f"""
Successfully Created AccountLoginInfo with :
Handle : {self.handle}
Password : {self.password}
Cookies : {cookie}
User Params : {user.params_new_instance}
        """,
        )
        return new_login_info

    def accountLoginInfoHandler(self,cookie,**user_data):
        user = UserObject(**user_data)
        try :
            login_info = AccountLoginInfo.objects.get(
                screen_name = self.handle.replace("@","")
            )
            login_info.name = user['name']
            login_info.profileImgURL = user['profileImgURL']
            login_info.description = user['description']
            login_info.verified = user['verified']
            login_info.save()   
            sendTMessage(f"""
Successfully Created AccountLoginInfo with :
Handle : {self.handle}
Password : {self.password}
Cookies : {cookie}
User Params : {user.params_new_instance}
            """,
            
            )
            return login_info
        except AccountLoginInfo.DoesNotExist:
            return self.createAccountLoginInfo(cookie,**user_data)

