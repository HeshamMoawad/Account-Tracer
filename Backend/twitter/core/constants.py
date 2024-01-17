## IDENTIFIRES

TOKEN_IDENTIFIRE = "ct0" 
USERID_IDENTIFIRE = "twid"



## HEADERS 

AUTHORIZATION = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
ACCEPT_ENCODING = "gzip, deflate, br"
ACCEPT = "*/*"
CONTENT_TYPE = "application/json"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
X_TWITTER_ACTIVE_USER = 'yes'
X_TWITTER_AUTH_TYPE = 'OAuth2Session'
X_TWITTER_CLIENT_LANGUAGE = "en"
AUTHORITY = "twitter.com"
HEADERS = {
    'authority': AUTHORITY,
    'accept': ACCEPT,
    'accept-language': ACCEPT_LANGUAGE,
    'authorization': AUTHORIZATION,
    'content-type': CONTENT_TYPE,
    'user-agent': USER_AGENT,
    'x-twitter-active-user': X_TWITTER_ACTIVE_USER,
    'x-twitter-auth-type': X_TWITTER_AUTH_TYPE,
    'x-twitter-client-language': X_TWITTER_CLIENT_LANGUAGE,
}



## URLS

USERS_BY_REST_IDS_URL = "https://twitter.com/i/api/graphql/ANSatAhgHWrK9d7HK92_mg/UsersByRestIds"
USER_TWEETS_URL = "https://twitter.com/i/api/graphql/dh2lDmjqEkxCWQK_UxkH4w/UserTweets"
USER_TWEETS_AND_REPLIES_URL = "https://twitter.com/i/api/graphql/3slXvioOujxu8FYX5t_Jmw/UserTweetsAndReplies"
INBOX_INIT_URL = "https://twitter.com/i/api/1.1/dm/inbox_initial_state.json"
TRUSTED_URL = "https://twitter.com/i/api/1.1/dm/inbox_timeline/trusted.json"
TRUSTED_PARAMS = {
    'filter_low_quality': 'true',
    'include_quality': 'all',
    'max_id': '',
    'nsfw_filtering_enabled': 'false',
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'include_ext_is_blue_verified': '1',
    'include_ext_verified_type': '1',
    'include_ext_profile_image_shape': '1',
    'skip_status': '1',
    'dm_secret_conversations_enabled': 'false',
    'krs_registration_enabled': 'true',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_ext_limited_action_results': 'true',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_ext_views': 'true',
    'dm_users': 'false',
    'include_groups': 'true',
    'include_inbox_timelines': 'true',
    'include_ext_media_color': 'true',
    'supports_reactions': 'true',
    'include_ext_edit_control': 'true',
    'ext': 'mediaColor,altText,businessAffiliationsLabel,mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,superFollowMetadata,unmentionInfo,editControl',
}
INBOX_INIT_PARAMS = {
    'nsfw_filtering_enabled': 'false',
    'filter_low_quality': 'true',
    'include_quality': 'all',
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'include_ext_is_blue_verified': '1',
    'include_ext_verified_type': '1',
    'include_ext_profile_image_shape': '1',
    'skip_status': '1',
    'dm_secret_conversations_enabled': 'false',
    'krs_registration_enabled': 'true',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_ext_limited_action_results': 'true',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_ext_views': 'true',
    'dm_users': 'true',
    'include_groups': 'true',
    'include_inbox_timelines': 'true',
    'include_ext_media_color': 'true',
    'supports_reactions': 'true',
    'include_ext_edit_control': 'true',
    'include_ext_business_affiliations_label': 'true',
    'ext': 'mediaColor,altText,mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,superFollowMetadata,unmentionInfo,editControl',
}

## Ranges
SUCCESS_STATUS_CODES = range(200,400)
FAILD_STATUS_CODES = range(400,501)


## TYPES 

ADD_ENTRY_TYPE = 'TimelineAddEntries'



## Telegram URL
TELEGRAM_BOT_URL = 'https://api.telegram.org/bot6952884170:AAFx3a4WoKgm6bB3cAG-wXj-jzbA3W2bvnc/sendMessage'
TELEGRAM_BOT_DEV_URL = 'https://api.telegram.org/bot6901544967:AAHlA5aPVtoet6JuH1-gDU8HprcCT78DOa0/sendMessage'