
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
from core.utils import *

logging.getLogger('seleniumwire').setLevel(logging.WARNING)

class LoginUsingBrowser(object):
    LOGINURL = "https://twitter.com/i/flow/login"
    USERNAMEXPATH = """//input[@autocomplete="username"]"""
    NEXTBUTTONXPATH = """//div[@role="button"]//div[@dir="ltr"]//span//span[text()="Next"]"""
    PASSWORDXPATH = """//input[@autocomplete="current-password"]"""
    LOGINBUTTONXPATH = """//div[@role="button"]//div[@dir="ltr"]//span//span[text()="Log in"]""" 
    confirmLOGINXPATH = """//div[@role="presentation"]"""
    
    def login(self , UserName,Password )-> Union[dict,None] :
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-logging')
        print(chrome_options.arguments)
        try :
            self.driver = webdriver.Chrome(options = chrome_options)
            self.driver.minimize_window()
            self.driver.get('https://twitter.com/login')
            print("browser opened")
            self.wait_element(self.USERNAMEXPATH).send_keys(UserName)
            print("send user")
            self.wait_element(self.NEXTBUTTONXPATH).click()
            print("click next")
            self.wait_element(self.PASSWORDXPATH).send_keys(Password)
            print("send pass")
            self.wait_element(self.LOGINBUTTONXPATH).click()
            print("click login")
            self.wait_element(self.confirmLOGINXPATH)
            print("confirm login")
            self.driver.get(f"https://twitter.com/{UserName}")
            print("get profile")
            req = self.driver.wait_for_request("/UserByScreenName").headers
            cookies = req['cookie']
            # cookies = self.driver.execute_script("return document.cookie;")
            print(f"\n{req}\n")
            self.driver.quit()
            return dict( 
                cookie = cookies,
                username = UserName ,
                password = Password 
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
        return self.waiting.until(EC.presence_of_element_located(arg))





