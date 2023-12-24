from .models import TwitterAbstractSession , TweetsParser
from .constants import (
    USERS_BY_REST_IDS_URL,
    USER_TWEETS_AND_REPLIES_URL ,
    SUCCESS_STATUS_CODES
    )
# from easydict import EasyDict
import typing , datetime


class TwitterSession(TwitterAbstractSession):


    def __init__(self, cookies: str) -> None:
        super().__init__(cookies)

    def getMe(self):
        params = {
            'variables': '{"userIds":["$$$$"]}'.replace("$$$$",self.parser.userID),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        }
        response =  self.get( url = USERS_BY_REST_IDS_URL , params = params)
        print(response)
        return response.json()


    def getMyTweets(self,_from:datetime.datetime ,_to:datetime.datetime=datetime.datetime.today()):
        stop = False
        cursor = None
        tweets:typing.List[dict] = []
        while not stop :
            parser = self._getMyTweets(cursor=cursor)
            tweets += parser.tweets
            cursor = parser.bottomCursor
            date = parser.createdAtParser(parser.tweets[-1])
            print( _from.date() ,date.date(),_to.date() ,date.date() >= _to.date())
            if (date.date() >= _from.date()):
                # print(parser.createdAtParser(tweets[0]))
                stop = True
                break
        
        return TweetsParser().filterBetween(tweets,_from=_from)
        


    def _getMyTweets(
            self,
            count:int=40 , 
            cursor:typing.Union[str,None]=None ,

                )-> typing.Union[TweetsParser,None]:

        params = { 
            'variables': '{"userId":"$$$$","count":####,@@@@"includePromotedContent":true,"withCommunity":true,"withVoice":true,"withV2Timeline":true}'\
                .replace("$$$$",self.parser.userID) \
                    .replace("####",str(count)) \
                        .replace("@@@@",'' if isinstance(cursor , type(None)) else f'"cursor":"{cursor}",')
                    ,
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = self.get(USER_TWEETS_AND_REPLIES_URL,params=params)
        if response.status_code in SUCCESS_STATUS_CODES:
            parser = TweetsParser(response.json())
            return parser #parser.filterBetween(parser.tweets)
        else :
            return None