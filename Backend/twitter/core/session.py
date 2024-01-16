from .models import (
    TweetsParser,
    ChatsParser ,
)
from .abstract import TwitterAbstractSession
from .objects import  (
    TweetObject ,
    ReplyObject ,
    )
from .constants import (
    USERS_BY_REST_IDS_URL,
    USER_TWEETS_AND_REPLIES_URL,
    SUCCESS_STATUS_CODES,
    INBOX_INIT_URL,
    INBOX_INIT_PARAMS,
    TRUSTED_URL,
    TRUSTED_PARAMS,
)
# from .utils import save
from ..models import (
    Chat, 
    AccountLoginInfo , 
    Tweet , 
    Reply , 
    MediaLink )
import typing
import datetime 


class TwitterSession(TwitterAbstractSession):

    def __init__(self, cookies: str , max_older : datetime.datetime = datetime.datetime.now()-datetime.timedelta(days=-2)) -> None:
        super().__init__(cookies)
        self.account_model = AccountLoginInfo.objects.filter(rest_id=self.parser.userID).first().account
        self.max_older = max_older

    def getMe(self):
        params = {
            'variables': '{"userIds":["$$$$"]}'.replace("$$$$", self.parser.userID),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        }
        response = self.get(url=USERS_BY_REST_IDS_URL, params=params)
        if response[response.StatusCodeTypes.OK]:
            return response.json()
        elif response[response.StatusCodeTypes.FORBIDDEN]:
            return {}
        else:
            print(response)
            return {"message" : response.text }

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


    def __getMyTweets(
            self,
            count: int = 40,
            cursor: typing.Union[str, None] = None,

    ) -> typing.Union[TweetsParser, None]:

        params = {
            'variables': '{"userId":"$$$$","count":####,@@@@"includePromotedContent":true,"withCommunity":true,"withVoice":true,"withV2Timeline":true}'
            .replace("$$$$", self.parser.userID)
            .replace("####", str(count))
            .replace("@@@@", '' if isinstance(cursor, type(None)) else f'"cursor":"{cursor}",'),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = self.get(USER_TWEETS_AND_REPLIES_URL, params=params)
        if response.status_code in SUCCESS_STATUS_CODES:
            return TweetsParser(response.json())


    def __init_Inbox(self):
        params = INBOX_INIT_PARAMS.copy()
        response = self.get(
            url=INBOX_INIT_URL,
            params=params
        )
        # print(response)
        if response[response.StatusCodeTypes.OK]:
            return ChatsParser(response.json(), parse_date=None)

    def __trusted(self, next_entry_id: str):
        params = TRUSTED_PARAMS.copy()
        params.update({
            "max_id": next_entry_id
        })
        response = self.get(
            url=TRUSTED_URL,
            params=params
        )
        # print(response)
        if response[response.StatusCodeTypes.OK]:
            return ChatsParser(response.json(), parse_date=None)
    
    def __saveObject(self, model,instance):
        obj, created = model.objects.get_or_create(
            account = self.account_model ,
            **instance.data
        )
        if created:
            obj.save()
        return obj

    def __saveObjects(self, model,iterable:typing.Iterable):
        for it in iterable:
            self.__saveObject(model,it)

    def __saveReply(self,reply:ReplyObject):
        obj:Reply = self.__saveObject(Reply,reply)
        if reply.replied_from :
            obj.replied_from = self.__saveReply(reply.replied_from)
        links = reply.media_links()
        if links :
            for link in links :
                media_obj , created = MediaLink.objects.get_or_create(url=link)
                if created :
                    media_obj.save()
                    obj.media_links.add(media_obj)
        obj.save()
        return obj

    def __saveTweet(self,tweet:TweetObject):
        obj:Tweet = self.__saveObject(Tweet,tweet)
        if tweet.quoted_retweted_from :
            obj.quoted_retweted_from = self.__saveTweet(tweet.quoted_retweted_from)
        if tweet.retweted_from :
            obj.retweted_from = self.__saveTweet(tweet.retweted_from)
        links = tweet.media_links()
        if links :
            for link in links :
                media_obj , created = MediaLink.objects.get_or_create(url=link)
                if created :
                    media_obj.save()
                    obj.media_links.add(media_obj)
        obj.save()
        return obj
