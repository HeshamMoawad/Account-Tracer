from .abstract import TwitterBaseSession
from .objects import UserObject
from ..models import (
    Chat,
    FollowUnFollow,
)
# import datetime


class TwitterSession(TwitterBaseSession):

    def saveMyStats(self):
        result = self._getMe()
        if result:
            users = result.get("data", {}).get("users", [])
            if users:
                user = UserObject(**users[0].get("result"))
                record = FollowUnFollow.objects.create(
                    account=self.account_model,
                    followers=user.followers,
                    following=user.following,
                    likes=user.likes
                )
                record.save()
                self.login_info_model.name = user['name']
                self.login_info_model.profileImgURL = user['profileImgURL']
                self.login_info_model.description = user['description']
                self.login_info_model.verified = user['verified']
                self.login_info_model.save()
                print(f"[+]\t({self.account_model.handle}) : Status {user.followers} Followers {user.following} Following {user.likes} Likes ")

    def saveMyTweets(self, _cursor=None, _con=False):
        if _cursor or not _con:
            tweet_parser = self._getMyTweets(cursor=_cursor)
            if tweet_parser:
                tweets = tweet_parser.tweets
                replies = tweet_parser.replies
                [self._saveTweet(tweet) for tweet in tweets]
                [self._saveReply(reply) for reply in replies]
                print(f"[+]\t({self.account_model.handle}) : Collected {len(tweets)} Tweets {len(replies)} Replies ")
                if not tweets[-1].created_at.date() <= self.max_older.date():
                    _cursor = tweet_parser.getValueFromCursor(
                        tweet_parser.bottomCursor)
                    self.saveMyTweets(
                        _cursor=_cursor,
                        _con=True
                    )

    def saveMyChats(self, initial=None, con=False):
        if not initial and not con:
            initial = self._init_Inbox()
        if initial:
            conversations = initial.conversations
            self._saveObjects(Chat,conversations )
            print(f"[+]\t({self.account_model.handle}) : Collected Init {len(conversations)} Chats  ")
            if initial.next_entry_id:
                trusted = self._trusted(next_entry_id=initial.next_entry_id)
                if trusted:
                    conversations = trusted.conversations
                    self._saveObjects(Chat, conversations)
                    print(f"[+]\t({self.account_model.handle}) : Collected Trusted {len(conversations)} Chats  ")
                    if len(trusted.conversations) >= 1 and not trusted.conversations[-1].chat_datetime.date() <= self.max_older.date():
                        if trusted.next_entry_id:
                            self.saveMyChats(trusted, con=True)
