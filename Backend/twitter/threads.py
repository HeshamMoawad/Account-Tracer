from .core.userModel import User
from .core.utils import CookiesParser
from .core.session import TwitterSession
from .models import TwitterAccount , AccountLoginInfo
from .TWlogin import LoginUsingBrowser
from threading import Thread 



# def threadedFuncLogin(instance:TwitterAccount): 
    # handle = str(instance.handle)
    # password = str(instance.password)
    # print(instance , handle , password,sep="\n")
    # try :
    #     browser = LoginUsingBrowser()
    #     result = browser.login(handle , password , logging_with_print=False)
        # print(result)
        # if isinstance(result , dict):
        #     session = TwitterSession(result.get("cookie"))
        #     accountResponse = session.getMe()
            # print(accountResponse)
    #         user_data = accountResponse["data"]["users"]
    #         if user_data :
    #             user_data = user_data[0]["result"]
    #             user = User(**user_data)
    #             new_login_info = AccountLoginInfo.objects.create(
    #                 account = instance ,
    #                 cookies = result['cookie'] ,
    #                 token = CookiesParser(result['cookie']).token,
    #                 **user.params_new_instance
    #             )
    #             new_login_info.save()
    #             print("\nSaved\n")
    #     else :
    #         instance.delete()
    #         print("\nDeleted\n")
    # except Exception as e :
    #     print(f"\nError in Thread {currentThread().name} - {e}\n")



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
                    self.createSession(response['cookie'])
        except Exception as e :
            print(e)

    def createSession(self,cookie:str):
        session = TwitterSession(cookie)
        me = session.getMe()
        user_data = me["data"]["users"]
        if user_data :
            user_data = user_data[0]["result"]
            user = User(**user_data)
            new_login_info = AccountLoginInfo.objects.create(
                account = self.instance ,
                cookies = cookie ,
                token = CookiesParser(cookie).token,
                **user.params_new_instance
            )
            new_login_info.save()
            print("\nSaved\n")


