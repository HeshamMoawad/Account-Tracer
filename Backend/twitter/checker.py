from .models import AccountLoginInfo
from .core.session import TwitterSession 
from .TWlogin import LoginUsingBrowser
from .core.userModel import User
from .core.utils import CookiesParser




class CheckLoggedAccount(object):
    def __init__(self,instance:AccountLoginInfo) -> None:
        self.instance = instance
        self.handle = instance.account.handle
        self.password = instance.account.password 
        self.check()
        
    def check(self):
        resault = self.createSession(self.instance.cookies)
        if resault :
            self.updateInstance(resault,self.instance.cookies)
        else :
            self.makeNewLogin(self.handle,self.password)
    

    def makeNewLogin(self,handle,password) -> None:
        try :
            browser = LoginUsingBrowser()
            response = browser.login(handle,password)
            if isinstance(response , dict):
                    self.createSession(response['cookie'])
            else :
                # self.instance.delete()
                pass
        except Exception as e :
            print(e)


    def createNewInstance(self,response,cookie):
        user_data = response["data"]["users"]
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

    def updateInstance(self,response,cookie):
        user_data = response["data"]["users"]
        if user_data :
            user_data = user_data[0]["result"]
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
            except AccountLoginInfo.DoesNotExist:
                self.createNewInstance(response,cookie)
            print("\nSaved\n")

    def createSession(self,cookie:str)-> dict:
        session = TwitterSession(cookie)
        return session.getMe()
            









