import typing , traceback , datetime
from urllib.parse import unquote
from http.cookies import SimpleCookie
from .objects import ChatDetails , ReplyObject , TweetObject
from .constants import (
    ADD_ENTRY_TYPE,
    TOKEN_IDENTIFIRE, 
    USERID_IDENTIFIRE
)


class CookiesParser(object):
    def __init__(self, cookies) -> None:
        self.simplecookie = SimpleCookie()
        self.simplecookie.load(cookies)
        self.cookies_as_dict = {k: v.value for k,
                                v in self.simplecookie.items()}

    @property
    def token(self):
        return unquote(self.cookies_as_dict[TOKEN_IDENTIFIRE])

    @property
    def userID(self):
        return unquote(self.cookies_as_dict[USERID_IDENTIFIRE]).split("=")[-1]


class AbstractParser(object):

    @staticmethod
    def createdAtParser(legacy: dict) -> datetime.datetime:
        return datetime.datetime.strptime(legacy['created_at'], "%a %b %d %H:%M:%S %z %Y")

    def getInstructionsFromResponse(self, data: dict) -> list:
        if "data" in data.keys():
            data = data['data']
        if data:
            instructions = data['user']['result']['timeline_v2']['timeline']['instructions']
            return instructions
        else:
            return None

    def getEntriesFromInstractions(self, instructions: list) -> typing.Optional[list]:
        instract = None
        for inst in instructions:
            if inst['type'] == ADD_ENTRY_TYPE:
                instract = inst
                break
        return instract['entries']

    def getTweetsRepliesCursors(self, entries: typing.List[dict]) -> typing.Tuple[typing.List[dict], typing.List[dict], dict]:
        tweets = []
        replies = []
        cursors = {'top': None, 'bottom': None}
        for entry in entries:
            if 'tweet' in entry['entryId']:
                tweets.append(entry)
            elif 'profile-conversation' in entry['entryId']:
                replies.append(entry)
            elif 'cursor' in entry['entryId']:
                if 'cursor-top' in entry['entryId']:
                    cursors.update({"top": entry})
                elif 'cursor-bottom' in entry['entryId']:
                    cursors.update({"bottom": entry})
        return tweets, replies, cursors

    def getLegacyFromTweets(self, tweets: typing.List[dict]) -> typing.List[TweetObject]:
        legacies = []
        for tweet in tweets:
            try:
                legacy = tweet['content']['itemContent']['tweet_results']['result']['legacy']
                quoted = tweet['content']['itemContent']['tweet_results']['result'].get(
                    'quoted_status_result', None)
                legacies.append(TweetObject(legacy, quoted))
            except Exception as e:
                print(f"\n[-]\tError in : {e} \n==> {tweet}")
                traceback.print_exc()
        return legacies

    def getLegacyFromReplies(self, replies: typing.List[dict]) -> typing.List[ReplyObject]:
        legacies = []
        for reply in replies:
            try:
                legacy = reply['content']['items'][-1]['item']['itemContent']['tweet_results']['result']['legacy']
                replied_from = reply['content']['items'][-2]['item']['itemContent']['tweet_results']['result']['legacy'] if len(
                    reply['content']['items']) >= 2 else None
                legacies.append(ReplyObject(legacy, replied_from))
            except Exception as e:
                print(f"\n[-]\tError in : {e} \n==> {reply}")
                traceback.print_exc()
        return legacies

    def getValueFromCursor(self, cursor: dict) -> str:
        return cursor['content']['value']

    def checkDateFromLegacy(self, legacy: dict, _from: datetime.datetime = None, _to: datetime.datetime = datetime.datetime.today()):
        if not _from:
            _from = _to
        if legacy:
            return (_from.date() <= self.createdAtParser(legacy).date() <= _to.date())
        else:
            return False


class TweetsParser(AbstractParser):

    def __init__(self, data: dict = None) -> None:
        self.data = data
        if data:
            self.instructions = self.getInstructionsFromResponse(data)
            self.entries = self.getEntriesFromInstractions(self.instructions)
            self.__tweets, self.__replies, self.__cursors = self.getTweetsRepliesCursors(
                self.entries)
            self.bottomCursor = self.__cursors['bottom']
            self.topCursor = self.__cursors['top']
            self.tweets = self.getLegacyFromTweets(self.__tweets)
            self.replies = self.getLegacyFromReplies(self.__replies)

    def filterBetween(
        self,
        legaciesList: typing.List[dict],
        _from: datetime.datetime = None,
        _to: datetime.datetime = datetime.datetime.today(),
    ) -> typing.List[dict]:

        return list(filter(lambda x: self.checkDateFromLegacy(x, _from=_from, _to=_to), legaciesList))


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
        conversations_as_dict = self.response.get(
            str(self.type)).get("conversations")
        if self.type and conversations_as_dict:

            self.conversations: typing.List[ChatDetails] = list(map(
                lambda chat: ChatDetails(
                    data=conversations_as_dict[chat]
                ),
                conversations_as_dict.keys()
            ))
            if parse_date:
                self.conversations = list(filter(
                    lambda x: x.chat_datetime.date() == parse_date.date(), self.conversations))
        if self.conversations:
            self.next_entry_id = self.get_next_entry_id()

    def get_next_entry_id(self) -> typing.Optional[str]:
        try:
            if self.type == self.INIT:
                return str(self.response.get(str(self.type)).get("inbox_timelines").get("trusted").get("min_entry_id"))
            else:
                return str(self.response.get(str(self.type)).get("min_entry_id"))
        except KeyError:
            ...
