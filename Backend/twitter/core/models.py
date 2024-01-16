from django.utils import timezone
import typing  , datetime
from .abstract import AbstractParser




class TweetsParser(AbstractParser):

    def __init__(self, data:dict = None ) -> None:
        self.data = data
        if data :
            self.instructions = self.getInstructionsFromResponse(data)
            self.entries = self.getEntriesFromInstractions(self.instructions)
            self.__tweets , self.__replies , self.__cursors  = self.getTweetsRepliesCursors(self.entries)
            self.bottomCursor = self.__cursors['bottom']
            self.topCursor = self.__cursors['top']
            self.tweets = self.getLegacyFromTweets(self.__tweets)
            self.replies = self.getLegacyFromReplies(self.__replies)



    def filterBetween(
            self,
            legaciesList:typing.List[dict],
            _from:datetime.datetime=None ,
            _to:datetime.datetime=datetime.datetime.today() ,
                )->typing.List[dict]:

        return list(filter(lambda x : self.checkDateFromLegacy(x,_from=_from,_to=_to) , legaciesList))
        


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


class ChatsParser(object):
    INIT = "inbox_initial_state"
    TRUSTED = "inbox_timeline"

    def __init__(self, response: dict, parse_date: typing.Optional[datetime.datetime] = datetime.datetime.now()) -> None:
        self.conversations = []
        self.next_entry_id = None
        self.response = response
        try:
            self.type = list(response.keys())[0]
        except IndexError:
            self.type = None
        conversations_as_dict = self.response.get(str(self.type)).get("conversations")
        if self.type and conversations_as_dict:
            
            self.conversations: typing.List[ChatDetails] = list(map(
                lambda chat: ChatDetails(
                data = conversations_as_dict[chat]
                ), 
                conversations_as_dict.keys()
                ))
            if parse_date:
                self.conversations = list(filter(lambda x: x.chat_datetime.date() == parse_date.date(), self.conversations))
        if self.conversations:
            self.next_entry_id = self.get_next_entry_id()

    def get_next_entry_id(self) -> typing.Optional[str]:
        try:
            if self.type == self.INIT:
                return str(self.response.get(str(self.type)).get("inbox_timelines").get("trusted").get("min_entry_id"))
            else:
                return str(self.response.get(str(self.type)).get("min_entry_id"))
        except KeyError: ...


    