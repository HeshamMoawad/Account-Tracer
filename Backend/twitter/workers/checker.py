from ..models import AccountLoginInfo, TwitterAccount
from ..core.session import TwitterSession
from .TWlogin import LoginUsingBrowser
from ..core.userModel import User
from ..core.utils import CookiesParser
from threading import Thread
from typing import Optional


class BaseChecker(object):

    def makeNewLogin(self, twitter_account: TwitterAccount):
        try:
            browser = LoginUsingBrowser()
            return browser.login(
                twitter_account.handle,
                twitter_account.password
            )
        except Exception as e:
            print(e)

    def createNewInstance(self, instance: TwitterAccount, cookie, user: User):
        new_login_info = AccountLoginInfo.objects.create(
            account=instance,
            cookies=cookie,
            token=CookiesParser(cookie).token,
            **user.params_new_instance
        )
        new_login_info.save()
        print("\nSaved\n")

    def updateInstance(self, cookie: str, user: User, twitter_account: TwitterAccount) -> Optional[AccountLoginInfo]:
        try:
            login_info = AccountLoginInfo.objects.get(
                screen_name=twitter_account.handle.replace("@", "")
            )
            login_info.name = user['name']
            login_info.profileImgURL = user['profileImgURL']
            login_info.description = user['description']
            login_info.verified = user['verified']
            login_info.cookies = cookie
            login_info.token = CookiesParser(cookie).token
            login_info.save()
            print("\nSaved\n")
            return login_info
        except AccountLoginInfo.DoesNotExist:
            return

    def createTwitterSession(self, cookie: str) -> Optional[User]:
        session = TwitterSession(cookie)
        info = session.getMe()
        if info:
            user_data = info["data"]["users"]
            if user_data:
                user_data = user_data[0]["result"]
                return User(**user_data)


class CheckAccountLoginInfo(BaseChecker):

    def __init__(self, instance: AccountLoginInfo) -> None:
        self.instance = instance
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
                twitter_account=self.instance.account,
            )

    def runAsThread(self):
        Thread.__init__(self, target=self.fullCheck)
        self.start()


class CheckTwitterAccount(CheckAccountLoginInfo):

    def __init__(self, instance: TwitterAccount) -> None:
        BaseChecker.__init__(self)
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
