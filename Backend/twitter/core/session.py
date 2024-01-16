from .abstract import TwitterBaseSession
from ..models import (
    Chat, 
    AccountLoginInfo , )
import typing
import datetime 


class TwitterSession(TwitterBaseSession):

    def __init__(self, cookies: str , max_older : datetime.datetime = datetime.datetime.now()-datetime.timedelta(days=-2)) -> None:
        super().__init__(cookies)
        self.account_model = AccountLoginInfo.objects.filter(rest_id=self.parser.userID).first().account
        self.max_older = max_older

    def getMe(self): ...

    def saveMyTweets(self, _cursor=None, _con = False ):
        if _cursor or not _con:
            tweet_parser = self.__getMyTweets(cursor=_cursor)
            if tweet_parser :
                tweets = tweet_parser.tweets
                replies = tweet_parser.replies
                [self.__saveTweet(tweet) for tweet in tweets]
                [self.__saveReply(reply) for reply in replies]
                print(_cursor ,tweets[-1].created_at.date() , self.max_older.date() , tweets[-1].created_at.date() <= self.max_older.date() )
                if not tweets[-1].created_at.date() <= self.max_older.date() :
                    _cursor = tweet_parser.getValueFromCursor(tweet_parser.bottomCursor)
                    self.saveMyTweets(
                        _cursor=_cursor ,
                        _con=True
                    )

    def saveMyChats(self, initial=None, con=False ):
        if not initial and not con:
            initial = self.__init_Inbox()
        if initial:
            self.__saveObjects(Chat,initial.conversations)
            if initial.next_entry_id:
                trusted = self.__trusted(next_entry_id=initial.next_entry_id)
                if trusted:
                    self.__saveObjects(Chat,trusted.conversations)
                    if not trusted.conversations[-1].chat_datetime.date() <= self.max_older.date():
                        if trusted.next_entry_id:
                            self.saveMyChats(trusted, con=True)

