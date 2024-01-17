from requests import Session, Response
from .types import (
    HttpResponseTypes,
    HttpStatusCodeTypes,
)
from .objects import (
    ReplyObject,
    TweetObject
)
import typing
import datetime
from .parsers import (
    TweetsParser,
    ChatsParser,
    CookiesParser
)
from .constants import (
    USERS_BY_REST_IDS_URL,
    USER_TWEETS_AND_REPLIES_URL,
    SUCCESS_STATUS_CODES,
    INBOX_INIT_URL,
    INBOX_INIT_PARAMS,
    TRUSTED_URL,
    TRUSTED_PARAMS,
    HEADERS,
    ADD_ENTRY_TYPE

)
from ..models import (
    AccountLoginInfo,
    Tweet,
    Reply,
    MediaLink
)
import typing
import datetime


class TwitterAbastractResponse(Response):
    class Type(HttpResponseTypes):
        ...

    class StatusCodeTypes(HttpStatusCodeTypes):
        ...

    def __init__(self, response: Response, **kwargs) -> None:
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

    def __eq__(self, __o: typing.Any) -> bool:
        if isinstance(__o, TwitterAbastractResponse):
            return self.status_code_text == __o.status_code_text
        elif isinstance(__o, Response):
            return self.status_code == __o.status_code
        else:
            raise TypeError(
                f"Cannot compare with object of type {type(__o)}. Expected TwitterAbastractResponse or Response object.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(status_code={self.status_code},type={self.status_code_type},type_text={self.status_code_text})"

    def __getitem__(self, args: typing.Union[tuple, list]) -> bool:
        if isinstance(args, str):
            return self.status_code_type == args or self.status_code_text == args
        elif isinstance(args, tuple) or isinstance(args, list):
            return self.status_code_type in args or self.status_code_text in args
        else:
            raise TypeError(
                f"Cannot Check Type with object of type {type(args)}. Expected str or tuple or list object.")

    @property
    def status_code_type(self) -> Type:
        if self.status_code in self.__Informational.keys():
            return self.Type.INFORMATIONAL
        elif self.status_code in self.__Success.keys():
            return self.Type.SUCCESS
        elif self.status_code in self.__Redirect.keys():
            return self.Type.REDIRECT
        elif self.status_code in self.__ClientError.keys():
            return self.Type.CLIENTERROR
        elif self.status_code in self.__ServerError.keys():
            return self.Type.SERVERERROR
        else:
            return self.Type.UNKNOWN

    @property
    def status_code_text(self) -> str:
        if self.status_code in self.__Informational.keys():
            return self.__Informational[self.status_code]
        elif self.status_code in self.__Success.keys():
            return self.__Success[self.status_code]
        elif self.status_code in self.__Redirect.keys():
            return self.__Redirect[self.status_code]
        elif self.status_code in self.__ClientError.keys():
            return self.__ClientError[self.status_code]
        elif self.status_code in self.__ServerError.keys():
            return self.__ServerError[self.status_code]
        else:
            return self.Type.UNKNOWN

    def filterBOMchar(self) -> str:
        return self.text.lstrip('\ufeff')


class AbstractSession(Session):

    def __init__(self, cookies: str) -> None:
        super().__init__()
        self.cookies_str = cookies
        self.parser = CookiesParser(cookies)
        self.headers = HEADERS.copy()
        self.headers.update({"cookie": self.cookies_str})
        self.headers.update({"x-csrf-token": self.parser.token})
        self.headers.update({'referer': 'https://twitter.com/home'})
        # print(f"Headers : {self.headers}")

    def get(self, url: str,  params: dict = None, data=None, timeout: int = None, proxies: dict = None,  json: dict = None) -> TwitterAbastractResponse:
        try:
            return TwitterAbastractResponse(response=super().get(
                url,
                params=params,
                data=data,
                headers=self.headers,
                timeout=timeout,
                proxies=proxies,
                json=json,
            ))
        except Exception as e:
            print(f"[-]\tError : {e}")

    def post(self, url: str, data: dict = None, json: dict = None,  params: dict = None, timeout: int = None, proxies: dict = None) -> TwitterAbastractResponse:
        try:
            return TwitterAbastractResponse(response=super().post(
                url,
                params=params,
                data=data,
                headers=self.headers,
                timeout=timeout,
                proxies=proxies,
                json=json,
            ))
        except Exception as e:
            print(f"[-]\tError : {e}")


class TwitterBaseSession(AbstractSession):

    def __init__(self, cookies: str, max_older: datetime.datetime = datetime.datetime.now()-datetime.timedelta(days=-2)) -> None:
        super().__init__(cookies)
        self.login_info_model = AccountLoginInfo\
                                    .objects\
                                        .filter(rest_id=self.parser.userID)\
                                            .first()
        self.account_model = self.login_info_model.account
        self.max_older = max_older

    def _getMe(self):
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
            return {"message": response.text}

    def _getMyTweets(
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

    def _init_Inbox(self):
        params = INBOX_INIT_PARAMS.copy()
        response = self.get(
            url=INBOX_INIT_URL,
            params=params
        )
        if response[response.StatusCodeTypes.OK]:
            return ChatsParser(response.json(), parse_date=None)

    def _trusted(self, next_entry_id: str):
        params = TRUSTED_PARAMS.copy()
        params.update({
            "max_id": next_entry_id
        })
        response = self.get(
            url=TRUSTED_URL,
            params=params
        )
        if response[response.StatusCodeTypes.OK]:
            return ChatsParser(response.json(), parse_date=None)

    def _saveObject(self, model, instance , **kwargs ):
        data:dict = instance.data
        favorite_count = data.pop("favorite_count",None)
        reply_count = data.pop("reply_count",0)
        retweet_count = data.pop("retweet_count",0)
        bookmark_count = data.pop("bookmark_count",0)
        obj, created = model.objects.get_or_create(
            account=self.account_model,
            **data
        )
        if favorite_count:
            obj.favorite_count = favorite_count
            obj.reply_count = reply_count
            obj.retweet_count = retweet_count
            obj.bookmark_count = bookmark_count
        obj.save()
        return obj

    def _saveObjects(self, model, iterable: typing.Iterable):
        for it in iterable:
            self._saveObject(model, it)

    def _saveReply(self, reply: ReplyObject):
        obj: Reply = self._saveObject(Reply, reply)
        if reply.replied_from:
            obj.replied_from = self._saveReply(reply.replied_from)
        links = reply.media_links()
        if links:
            for link in links:
                media_obj, created = MediaLink.objects.get_or_create(url=link)
                if created:
                    media_obj.save()
                    obj.media_links.add(media_obj)
        obj.save()
        return obj

    def _saveTweet(self, tweet: TweetObject):
        obj: Tweet = self._saveObject(Tweet, tweet )
        if tweet.quoted_retweted_from:
            obj.quoted_retweted_from = self._saveTweet(
                tweet.quoted_retweted_from)
        if tweet.retweted_from:
            obj.retweted_from = self._saveTweet(tweet.retweted_from)
        links = tweet.media_links()
        if links:
            for link in links:
                media_obj, created = MediaLink.objects.get_or_create(url=link)
                if created:
                    media_obj.save()
                    obj.media_links.add(media_obj)
        obj.save()
        return obj
