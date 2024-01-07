
"""


{
"result": {
    "__typename": "User",
    "id": "VXNlcjoxNjk4NjAxNzcyNDMwODA3MDQw",
    "rest_id": "1698601772430807040",
    "affiliates_highlighted_label": {},
    "has_graduated_access": true,
    "is_blue_verified": false,
    "profile_image_shape": "Circle",
    "legacy": {
        "can_dm": true,
        "can_media_tag": true,
        "created_at": "Mon Sep 04 07:40:07 +0000 2023",
        "default_profile": true,
        "default_profile_image": false,
        "description": "تابع الحساب ( follow)\n العالميه لتداول الاسواق الماليه السعودي وادراة المحافظ\nتابع معنا النتائج #تاسي \n#بنك_الراجحي",
        "entities": {
            "description": { "urls": [] },
            "url": {
            "urls": [
                {
                "display_url": "al3alamia.info/register/109",
                "expanded_url": "https://al3alamia.info/register/109",
                "url": "https://t.co/QcWsOWb66s",
                "indices": [0, 23]
                }
            ]
            }
        },
        "fast_followers_count": 0,
        "favourites_count": 15,
        "followers_count": 65,
        "friends_count": 828,
        "has_custom_timelines": false,
        "is_translator": false,
        "listed_count": 0,
        "location": " saudi arabia ",
        "media_count": 65,
        "name": "ابو على",
        "needs_phone_verification": false,
        "normal_followers_count": 65,
        "pinned_tweet_ids_str": ["1727373626331353116"],
        "possibly_sensitive": false,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1698601772430807040/1696311851",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1709082213935964160/DSnPB2DY_normal.jpg",
        "profile_interstitial_type": "",
        "screen_name": "alashm27914",
        "statuses_count": 273,
        "translator_type": "none",
        "url": "https://t.co/QcWsOWb66s",
        "verified": false,
        "want_retweets": false,
        "withheld_in_countries": []
    }
}
}

                    # rest_id = user_data.get("rest_id",f"faild_parse rest_id {instance.handle}") , 
                    # name = user_data.get("name",f"faild_parse name {instance.handle}") , 
                    # screen_name = user_data.get("name",f"faild_parse name {instance.handle}") , 
                    # description =
                    # profileImgURL = 
                    # verified =
                    ******* cookies = 
                    ******* token = 
                    # suspend = 
                    created_at = 


"""
    


class User(object):
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
            "suspend" : bool(legacy.get("suspended",False)) ,
            "created_at" : bool(legacy.get("created_at",""))
        })

