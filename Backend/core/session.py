from .models import TwitterAbstractSession
from .constants import (
    USERS_BY_REST_IDS_URL,
    USER_TWEETS_URL
    )
from easydict import EasyDict
import typing


class TwitterSession(TwitterAbstractSession):
    def __init__(self, cookies: str) -> None:
        super().__init__(cookies)

    def getMe(self)-> EasyDict:
        params = {
            'variables': '{"userIds":["$$$$"]}'.replace("$$$$",self.parser.userID),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        }
        # print(f"Params : {params}")
        response =  self.get( url = USERS_BY_REST_IDS_URL , params = params)
        print(response)
        return response.json().data.users[0]


    def getTweets(self):
        pass


    def _getTweets(self,count:int=20 , cursor:typing.Union[str,None]=None)-> EasyDict:
        params = { # DAABCgABGBED0XCATiIKAAIYEOZSGpeR2wgAAwAAAAEAAA
            'variables': '{"userId":"$$$$","count":####,@@@@"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'\
                .replace("$$$$",self.parser.userID) \
                    .replace("####",str(count)) \
                        .replace("@@@@",'' if isinstance(cursor , type(None)) else f'"cursor":"{cursor}",')
                    ,
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_home_pinned_timelines_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }

        print(params)
        response = self.get(USER_TWEETS_URL,params=params)
        print(response)
        return response.json().data.user.result