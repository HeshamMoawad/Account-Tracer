from requests import  Session , Response
from .constants import (
    HEADERS ,
)
from .utils import CookiesParser
from easydict import EasyDict
from .types import (
        HttpResponseTypes , 
        HttpStatusCodeTypes ,
    )
import typing


class TwitterAbastractResponse(Response):
    class Type(HttpResponseTypes): ...
    class StatusCodeTypes(HttpStatusCodeTypes): ...

    def __init__(self,response:Response,**kwargs) -> None:
        # super().__init__()
        self.__dict__ = response.__dict__
        # Information responses
        self.__Informational = self.Type.informational()
        # Successful responses
        self.__Success = self.Type.success()
        # Redirection messages
        self.__Redirect = self.Type.redirect()
        # Client error responses
        self.__ClientError = self.Type.clientError()
        # Server error responses
        self.__ServerError = self.Type.serverError()
    
    def __eq__(self, __o:typing.Any) -> bool:
        if isinstance(__o,TwitterAbastractResponse):
            return self.status_code_text == __o.status_code_text
        elif isinstance(__o,Response) :
            return self.status_code == __o.status_code
        else :
            raise TypeError(f"Cannot compare with object of type {type(__o)}. Expected NewResponse or Response object.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(status_code={self.status_code},type={self.status_code_type},type_text={self.status_code_text})"

    def __getitem__(self,args:typing.Union[tuple,list])->bool:
        if isinstance(args,str):return self.status_code_type == args or self.status_code_text == args
        elif isinstance(args,tuple) or isinstance(args,list):return self.status_code_type in args or self.status_code_text in args
        else : raise TypeError(f"Cannot Check Type with object of type {type(args)}. Expected str or tuple or list object.")

    @property
    def status_code_type(self)->Type:
        if self.status_code in self.__Informational.keys() : 
            return self.Type.INFORMATIONAL
        elif self.status_code in self.__Success.keys() : 
            return self.Type.SUCCESS
        elif self.status_code in self.__Redirect.keys() : 
            return self.Type.REDIRECT
        elif self.status_code in self.__ClientError.keys() : 
            return self.Type.CLIENTERROR
        elif self.status_code in self.__ServerError.keys() : 
            return self.Type.SERVERERROR
        else : return self.Type.UNKNOWN
    
    @property
    def status_code_text(self)->str :
        if self.status_code in self.__Informational.keys() : 
            return self.__Informational[self.status_code]
        elif self.status_code in self.__Success.keys() : 
            return self.__Success[self.status_code]
        elif self.status_code in self.__Redirect.keys() : 
            return self.__Redirect[self.status_code]
        elif self.status_code in self.__ClientError.keys() : 
            return self.__ClientError[self.status_code]
        elif self.status_code in self.__ServerError.keys() : 
            return self.__ServerError[self.status_code]
        else : return self.Type.UNKNOWN
 
    def filterBOMchar(self)->str:
        return self.text.lstrip('\ufeff')

    def json(self)->EasyDict:
        return EasyDict(super().json())




class TwitterAbstractSession(Session): 

    def __init__(self , cookies:str) -> None:
        super().__init__()
        self.cookies_str = cookies
        self.parser = CookiesParser(cookies)
        self.headers = HEADERS.copy()
        self.headers.update({"cookie":self.cookies_str})
        self.headers.update({"x-csrf-token":self.parser.token})
        self.headers.update({'referer': 'https://twitter.com/home'})
        print(f"Headers : {self.headers}")


    def get(self, url:str ,  params:dict=None , data=None , timeout:int=None , proxies:dict=None,  json:dict=None ) -> TwitterAbastractResponse:
        try : 
            return TwitterAbastractResponse(response = super().get(
                url, 
                params=params, 
                data=data, 
                headers=self.headers, 
                timeout=timeout, 
                proxies=proxies, 
                json=json,
                ))
        except Exception as e :
            print(f"[-]\tError : {e}")


    def post(self, url: str , data:dict=None, json:dict=None,  params:dict=None, timeout:int=None, proxies:dict=None) -> TwitterAbastractResponse:
        try : 
            return TwitterAbastractResponse(response = super().post(
                url, 
                params=params, 
                data=data, 
                headers=self.headers, 
                timeout=timeout, 
                proxies=proxies, 
                json=json,
                ))
        except Exception as e :
            print(f"[-]\tError : {e}")









