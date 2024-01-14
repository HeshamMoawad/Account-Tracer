
from seleniumwire import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
from seleniumwire.webdriver import ChromeOptions
from typing import (
    Union
)
import logging 
from ..core.utils import *

# logging.getLogger('seleniumwire').setLevel(logging.WARNING)

class LoginUsingBrowser(object):
    LOGINURL = "https://twitter.com/i/flow/login"
    USERNAMEXPATH = """//input[@autocomplete="username"]"""
    NEXTBUTTONXPATH = """//div[@role="button"]//div[@dir="ltr"]//span//span[text()="Next"]"""
    PASSWORDXPATH = """//input[@autocomplete="current-password"]"""
    LOGINBUTTONXPATH = """//div[@role="button"]//div[@dir="ltr"]//span//span[text()="Log in"]""" 
    confirmLOGINXPATH = """//div[@role="presentation"]"""
    
    def login(self , UserName,Password , logging_with_print:bool = False)-> Union[dict,None] :
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-logging')
        print(chrome_options.arguments) if logging_with_print else None
        try :
            self.driver = webdriver.Chrome(options = chrome_options)
            self.driver.get('https://twitter.com/login')
            print("browser opened")  if logging_with_print else None
            self.wait_element(self.USERNAMEXPATH , timeout=100).send_keys(UserName)
            print("send user")  if logging_with_print else None
            self.wait_element(self.NEXTBUTTONXPATH , timeout=30).click()
            print("click next")  if logging_with_print else None
            self.wait_element(self.PASSWORDXPATH , timeout=30).send_keys(Password)
            print("send pass")  if logging_with_print else None
            self.wait_element(self.LOGINBUTTONXPATH , timeout=30).click()
            print("click login") if logging_with_print else None
            self.wait_element(self.confirmLOGINXPATH , timeout=30)
            print("confirm login")  if logging_with_print else None
            self.driver.get(f"https://twitter.com/{UserName}")
            print("get profile")  if logging_with_print else None
            req = self.driver.wait_for_request("/UserByScreenName").headers
            cookies = req['cookie']
            self.driver.quit()
            return dict( 
                cookie = cookies ,
                username = UserName ,
                password = Password ,
                )
        except Exception as e :
            print(e)
            try :
                self.driver.quit()
            except :
                pass
            return None




    def wait_element(self,val:str,by:str=By.XPATH,timeout:int=10)->WebElement:
        self.waiting = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.waiting.until(EC.visibility_of_element_located(arg))





