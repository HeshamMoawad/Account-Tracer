from requests import  Session , Response
from .utils import CookiesParser
from .types import (
    HttpResponseTypes , 
    HttpStatusCodeTypes ,
    )
from .constants import (
    HEADERS ,
    ADD_ENTRY_TYPE
)
from .objects import (
    ReplyObject ,
    TweetObject
    )
import typing , traceback , datetime


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
            raise TypeError(f"Cannot compare with object of type {type(__o)}. Expected TwitterAbastractResponse or Response object.")

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


class TwitterAbstractSession(Session): 

    def __init__(self , cookies:str) -> None:
        super().__init__()
        self.cookies_str = cookies
        self.parser = CookiesParser(cookies)
        self.headers = HEADERS.copy()
        self.headers.update({"cookie":self.cookies_str})
        self.headers.update({"x-csrf-token":self.parser.token})
        self.headers.update({'referer': 'https://twitter.com/home'})
        # print(f"Headers : {self.headers}")


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



class AbstractParser(object):

    @staticmethod
    def createdAtParser(legacy:dict)-> datetime.datetime:
        return datetime.datetime.strptime(legacy['created_at'], "%a %b %d %H:%M:%S %z %Y")


    def getInstructionsFromResponse(self,data:dict)->list:
        if "data" in data.keys(): data = data['data']
        if data:
            instructions = data['user']['result']['timeline_v2']['timeline']['instructions']
            return instructions
        else :
            return None


    def getEntriesFromInstractions(self,instructions:list) -> typing.Optional[list] :
        instract = None
        for inst in instructions :
            if inst['type'] == ADD_ENTRY_TYPE :
                instract = inst
                break
        return instract['entries']
    

    def getTweetsRepliesCursors(self,entries:typing.List[dict]) -> typing.Tuple[typing.List[dict],typing.List[dict],dict]:
        tweets = []
        replies = []
        cursors = {'top':None , 'bottom':None}
        for entry in entries:
            if 'tweet' in entry['entryId']:
                tweets.append(entry)
            elif 'profile-conversation' in entry['entryId'] :
                replies.append(entry)
            elif 'cursor' in entry['entryId'] :
                if 'cursor-top' in entry['entryId'] : cursors.update({"top":entry})
                elif 'cursor-bottom' in entry['entryId'] : cursors.update({"bottom":entry})
        return tweets , replies , cursors


    def getLegacyFromTweets(self,tweets:typing.List[dict])-> typing.List[TweetObject]:
        legacies = []
        for tweet in tweets : 
            try : 
                legacy = tweet['content']['itemContent']['tweet_results']['result']['legacy']
                quoted = tweet['content']['itemContent']['tweet_results']['result'].get('quoted_status_result',None)
                legacies.append(TweetObject(legacy,quoted))
            except Exception as e :
                print(f"\n[-]\tError in : {e} \n==> {tweet}")
                traceback.print_exc()
        return legacies
        

    def getLegacyFromReplies(self,replies:typing.List[dict]):
        legacies = []
        for reply in replies :
            try :
                legacy = reply['content']['items'][1]['item']['itemContent']['tweet_results']['result']['legacy']
                legacies.append(ReplyObject(legacy))
            except Exception as e :
                print(f"\n[-]\tError in : {e} \n==> {reply}")
                traceback.print_exc()
        return legacies


    def getValueFromCursor(self,cursor:dict) -> str :
        return cursor['content']['value']

    def checkDateFromLegacy(self,legacy:dict,_from:datetime.datetime=None , _to:datetime.datetime=datetime.datetime.today()):
        if not _from :  _from = _to
        if legacy :
            return (_from.date() <= self.createdAtParser(legacy).date() <= _to.date())
        else :
            return False
