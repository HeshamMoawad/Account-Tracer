from ..models import AccountLoginInfo, TwitterAccount
from ..core.session import TwitterSession
from .TWlogin import LoginUsingBrowser
from ..core.objects import UserObject
from ..core.parsers import CookiesParser
from ..core.utils import sendTMessage
from threading import Thread
from typing import Optional , Any


class BaseChecker(object):
    def __init__(self, instance:Any) -> None:
        self.instance = instance

    def makeNewLogin(self, twitter_account: TwitterAccount):
        try:
            browser = LoginUsingBrowser()
            return browser.login(
                twitter_account.handle,
                twitter_account.password
            )
        except Exception as e:
            sendTMessage(f"""
Faild Login as : {twitter_account.agent}
Username : {twitter_account.handle}
Password : {twitter_account.password}
            """)
            sendTMessage(f"""
Faild Login as : {twitter_account.agent}
Username : {twitter_account.handle}
Password : {twitter_account.password}
Error is {e}
            """,
            isDeveloper=True
            )
            print(e)

    def createNewInstance(self, instance: TwitterAccount, cookie, user: UserObject):
        new_login_info = AccountLoginInfo.objects.create(
            account=instance,
            cookies=cookie,
            token=CookiesParser(cookie).token,
            **user.params_new_instance
        )
        new_login_info.save()

    def updateInstance(self, cookie: str, user: UserObject, account_login_info: AccountLoginInfo) -> Optional[AccountLoginInfo]:
        try:
            account_login_info.name = user['name']
            account_login_info.profileImgURL = user['profileImgURL']
            account_login_info.description = user['description']
            account_login_info.verified = user['verified']
            account_login_info.cookies = cookie
            account_login_info.token = CookiesParser(cookie).token
            account_login_info.save()
            return account_login_info
        except AccountLoginInfo.DoesNotExist:
            return
        except Exception as e :
            sendTMessage(f"""
Faild updateInstance with Error \n{e}
            """,
            isDeveloper=True
            )
            return

    def createTwitterSession(self, cookie: str) -> Optional[UserObject]:
        session = TwitterSession(cookie)
        info = session._getMe()
        if info:
            user_data = info["data"]["users"]
            if user_data:
                user_data = user_data[0]["result"]
                return UserObject(**user_data)
            else :
                sendTMessage(f"""
Faild user_data with {user_data} 
                """,
                isDeveloper=True
                )
        else :
            sendTMessage(f"""
Faild _getMe with Response {info}
            """,
            isDeveloper=True
            )
    def __str__(self) -> str:
        return f"{self.__class__.__name__}( instance = {type(self.instance)} )"

class CheckAccountLoginInfo(BaseChecker):

    def __init__(self, instance : AccountLoginInfo) -> None:

        super().__init__( instance = instance )
        self.instance:AccountLoginInfo
        self.handle = self.instance.account.handle
        self.password = self.instance.account.password

    def fullCheck(self):
        if not self.checkCookie(self.instance.cookies):
            login = self.makeNewLogin(
                twitter_account=self.instance.account
            )
            if login:
                self.checkCookie(login['cookie'])

    def checkCookie(self, cookie: str):
        user = self.createTwitterSession(cookie)
        if user:
            return self.updateInstance(
                cookie=cookie,
                user=user,
                account_login_info=self.instance,
            )

    def runAsThread(self):
        Thread.__init__(self, target=self.fullCheck)
        self.start()


class CheckTwitterAccount(CheckAccountLoginInfo):

    def __init__(self, instance: TwitterAccount) -> None:
        BaseChecker.__init__(self , instance)
        loginInfos = AccountLoginInfo.objects.filter(account=instance)
        isExist = True if loginInfos.count() > 0 else False
        if isExist:
            super().__init__(loginInfos.first())
            self.fullCheck()
        else:
            login = self.makeNewLogin(twitter_account=instance)
            if login:
                user = self.createTwitterSession(login['cookie'])
                if user:
                    login_info = self.updateInstance(
                        cookie=login['cookie'],
                        user=user,
                        twitter_account=self.instance.account,
                    )
                    if login_info:
                        super().__init__(loginInfos.first())
                        self.fullCheck()
            else :
                sendTMessage(f"""
Account : {instance}
Handle : {instance.handle}
Password : {instance.password}
will Delete
please recheck Handle and Password
                """)
                instance.delete()