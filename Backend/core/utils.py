from urllib.parse import unquote
from http.cookies import re, SimpleCookie
from .constants import TOKEN_IDENTIFIRE , USERID_IDENTIFIRE


class CookiesParser(object):
    def __init__(self,cookies) -> None:
        self.simplecookie = SimpleCookie()
        self.simplecookie.load(cookies)
        self.cookies_as_dict = {k: v.value for k, v in self.simplecookie.items()}

    @property
    def token(self):
        return unquote(self.cookies_as_dict[TOKEN_IDENTIFIRE])
    @property
    def userID(self):
        return unquote(self.cookies_as_dict[USERID_IDENTIFIRE]).split("=")[-1]

