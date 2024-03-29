import typing , datetime
from django.utils import timezone

class UserObject(object):
    def __init__(self, **kwargs):
        self.params_new_instance = {}
        self.params_new_instance.update({
            "rest_id" : kwargs.get("rest_id") ,
        })
        legacy:dict = kwargs["legacy"]
        self.params_new_instance.update({
            "name" : legacy.get("name","Can't Parse") ,
            "screen_name" : legacy.get("screen_name",f"{self.params_new_instance.get('rest_id')}") ,
            "description" : legacy.get("description"," "),
            "profileImgURL" : legacy.get("profile_image_url_https"," ") ,
            "verified" : bool(legacy.get("verified",False)) ,
            "suspend" : bool(legacy.get("suspended",False))  ,
            "created_at" : datetime.datetime.strptime(legacy.get('created_at'), "%a %b %d %H:%M:%S %z %Y") ,
        })
        self.followers = legacy.get("followers_count",0) 
        self.following =  legacy.get("friends_count",0)
        self.likes = legacy.get("favourites_count",0)

    def __getitem__(self,__o:str):
        return self.params_new_instance.get(__o)



class TweetObject(object):
    def __init__(self, legacy:dict,quoted_status_result:dict=None) -> None:
        self.favorite_count = legacy.get("favorite_count",0)
        self.reply_count = legacy.get("reply_count" , 0)
        self.retweet_count = legacy.get("retweet_count" , 0)
        self.bookmark_count = legacy.get("bookmark_count",0)
        self.user_id_str = legacy.get("user_id_str")
        self.full_text = legacy.get("full_text","")
        self.extended_entities = legacy.get("extended_entities",None)
        self.created_at = datetime.datetime.strptime(legacy.get('created_at'), "%a %b %d %H:%M:%S %z %Y")
        self.conversation_id_str = legacy.get("conversation_id_str","")
        self.quoted_status_result = quoted_status_result
        self.retweeted_status_result = legacy.get("retweeted_status_result",None)

    def media_links(self)->typing.Optional[typing.List[str]]:
        if self.extended_entities:
            return [link.get("media_url_https") for link in self.extended_entities.get("media")]

    @property
    def quoted_retweted_from(self) -> typing.Optional['TweetObject']:
        if self.quoted_status_result :
            # print(self.quoted_status_result.keys())
            return TweetObject(self.quoted_status_result["result"]["legacy"])
    
    @property
    def retweted_from (self)  -> typing.Optional['TweetObject']:
        if self.retweeted_status_result :
            # print(self.retweeted_status_result["result"].keys())
            return TweetObject(self.retweeted_status_result["result"]["legacy"])

    @property
    def data(self):
        return {
            "favorite_count" : self.favorite_count ,
            "reply_count":self.reply_count ,
            "retweet_count":self.retweet_count,
            "bookmark_count":self.bookmark_count ,
            "user_id_str":self.user_id_str ,
            "full_text":self.full_text ,
            "created_at":self.created_at ,
            "conversation_id_str":self.conversation_id_str,
        }

class ReplyObject(TweetObject):
    def __init__(self, legacy: dict , replied_from:dict=None ) -> None:
        super().__init__(legacy)
        self.in_reply_to_screen_name = legacy.get("in_reply_to_screen_name",None)
        self.replied_from = None
        if replied_from:
            self.replied_from = ReplyObject(replied_from)
    @property
    def data(self):
        data = super().data
        data.update({
            "in_reply_to_screen_name":self.in_reply_to_screen_name
        })
        return data

class ChatDetails(object):
    def __init__(self, data: dict) -> None:
        self.conversation_id = data.get("conversation_id")
        self.chat_datetime = timezone.make_aware(datetime.datetime.fromtimestamp(float(float(data.get("sort_timestamp"))/1000))) 
        self.status = data.get("status")

    @property
    def data(self):
        return {
            "conversation_id":self.conversation_id ,
            "chat_datetime" : self.chat_datetime ,
            "status" : self.status
        }
