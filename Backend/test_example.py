import requests

# # cookies = {
# #     'guest_id': 'v1%3A169071146396654223',
# #     'kdt': 'MlFBbIWVrcyz4kpvoXV0lezJBLGlbZEVbxko36Mp',
# #     'auth_token': 'c5d4cd8cbf2e18b8bdd408abc5893ffde831e38b',
# #     'ct0': 'c62035c88ac4a4aae14ac18b4aeb59a762276ab5f18a4de90d2ec11b42661645152c7be3534d1f3c17b919bc17ab88c0890b507a0db531cfb0a2ca418693da6c60b295b7619d8100ee05a0e75c1b3a5d',
# #     'twid': 'u%3D1676505871419834368',
# #     'guest_id_marketing': 'v1%3A169071146396654223',
# #     'guest_id_ads': 'v1%3A169071146396654223',
# #     'twtr_pixel_opt_in': 'N',
# #     'des_opt_in': 'Y',
# #     'mbox': 'session#0919fa6238e34501a0fde6b1c06bbeed#1694593290|PC#0919fa6238e34501a0fde6b1c06bbeed.37_0#1757836230',
# #     '_ga_34PHSZMC42': 'GS1.1.1694588974.1.1.1694591435.0.0.0',
# #     '_ga': 'GA1.2.583746764.1690711461',
# #     'lang': 'en',
# #     '_gid': 'GA1.2.895367258.1702189270',
# #     'personalization_id': '"v1_mBu1Zu2PYWsqb/l6xWIuhA=="',
# # }

headers =  {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA', 
    'content-type': 'application/json', 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
    'x-twitter-active-user': 'yes', 
    'x-twitter-auth-type': 'OAuth2Session', 
    'x-twitter-client-language': 'en', 
    # 'cookie': 'guest_id_marketing=v1%3A170229621714088236; guest_id_ads=v1%3A170229621714088236; guest_id=v1%3A170229621714088236; gt=1734182143268397142; _ga=GA1.2.635252568.1702296226; _gid=GA1.2.2073304160.1702296226; ct0=ddb907d1545ccfdca3b4151c8aaee831d5ba439b8c45d3d16c931b40ddb52baeaab4724750421bb0fcc762621a301da339d9f0dbadcb67e632b549fcb56e68b8fc6a7333af7b7d316baa4346daeac96d; lang=en; twid=u%3D1698601772430807040; personalization_id="v1_RkT77nWTrkF2/HVc5foh+g=="', 
    # 'cookie': 'guest_id_marketing=v1%3A170229546626090505; guest_id_ads=v1%3A170229546626090505; guest_id=v1%3A170229546626090505; gt=1734178993845272726; _ga=GA1.2.2103778955.1702295478; _gid=GA1.2.755419721.1702295478; ct0=d1243f07ce0fa9ee95482d8fca130385082fcc72e4b5e48fe263a189a7a2053498dfd8fcee6a060ed785df39ef9f500ac153e8f2f23a0e4a718c32ddef5499361496a288c25fe0f2060f9e81f1c770e0; lang=en; personalization_id="v1_wSv6eFfVZJBYuQyuqC7g6A=="; twid=u%3D1698601772430807040',

    # 'x-csrf-token': 'd1243f07ce0fa9ee95482d8fca130385082fcc72e4b5e48fe263a189a7a2053498dfd8fcee6a060ed785df39ef9f500ac153e8f2f23a0e4a718c32ddef5499361496a288c25fe0f2060f9e81f1c770e0', 
    # 'x-csrf-token': 'd1243f07ce0fa9ee95482d8fca130385082fcc72e4b5e48fe263a189a7a2053498dfd8fcee6a060ed785df39ef9f500ac153e8f2f23a0e4a718c32ddef5499361496a288c25fe0f2060f9e81f1c770e0',

    'referer': 'https://twitter.com/home',
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',

    }


{
    # 'authority': 'twitter.com',
    # 'accept': '*/*',
    # 'accept-language': 'en-US,en;q=0.9',
    # 'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    # 'content-type': 'application/json',
    'cookie': 'guest_id=v1%3A169071146396654223; kdt=MlFBbIWVrcyz4kpvoXV0lezJBLGlbZEVbxko36Mp; auth_token=c5d4cd8cbf2e18b8bdd408abc5893ffde831e38b; ct0=c62035c88ac4a4aae14ac18b4aeb59a762276ab5f18a4de90d2ec11b42661645152c7be3534d1f3c17b919bc17ab88c0890b507a0db531cfb0a2ca418693da6c60b295b7619d8100ee05a0e75c1b3a5d; twid=u%3D1676505871419834368; guest_id_marketing=v1%3A169071146396654223; guest_id_ads=v1%3A169071146396654223; twtr_pixel_opt_in=N; des_opt_in=Y; mbox=session#0919fa6238e34501a0fde6b1c06bbeed#1694593290|PC#0919fa6238e34501a0fde6b1c06bbeed.37_0#1757836230; _ga_34PHSZMC42=GS1.1.1694588974.1.1.1694591435.0.0.0; _ga=GA1.2.583746764.1690711461; _gid=GA1.2.895367258.1702189270; lang=en; personalization_id="v1_Dh5Xjn+yaEnFbJwscTH0sg=="',
    # 'referer': 'https://twitter.com/home',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-csrf-token': 'c62035c88ac4a4aae14ac18b4aeb59a762276ab5f18a4de90d2ec11b42661645152c7be3534d1f3c17b919bc17ab88c0890b507a0db531cfb0a2ca418693da6c60b295b7619d8100ee05a0e75c1b3a5d',
    # 'x-twitter-active-user': 'yes',
    # 'x-twitter-auth-type': 'OAuth2Session',
    # 'x-twitter-client-language': 'en',
}

params = {
    'variables': '{"userIds":["1698601772430807040"]}',
    'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
} 

{'variables': '{"userIds":["1698601772430807040"]}', 'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}'}


response = requests.get(
    'https://twitter.com/i/api/graphql/ANSatAhgHWrK9d7HK92_mg/UsersByRestIds',
    params=params,
    headers=headers,
)

print(response)
print(response.text)
# print(response.json())


# from core.session import Session


# tt = Session('guest_id=v1:169071146396654223; kdt=MlFBbIWVrcyz4kpvoXV0lezJBLGlbZEVbxko36Mp; auth_token=c5d4cd8cbf2e18b8bdd408abc5893ffde831e38b; ct0=c62035c88ac4a4aae14ac18b4aeb59a762276ab5f18a4de90d2ec11b42661645152c7be3534d1f3c17b919bc17ab88c0890b507a0db531cfb0a2ca418693da6c60b295b7619d8100ee05a0e75c1b3a5d; twid=u=1676505871419834368; guest_id_marketing=v1:169071146396654223; guest_id_ads=v1:169071146396654223; twtr_pixel_opt_in=N; des_opt_in=Y; mbox=session#0919fa6238e34501a0fde6b1c06bbeed#1694593290|PC#0919fa6238e34501a0fde6b1c06bbeed.37_0#1757836230; _ga_34PHSZMC42=GS1.1.1694588974.1.1.1694591435.0.0.0; _ga=GA1.2.583746764.1690711461; _gid=GA1.2.895367258.1702189270; lang=en; personalization_id="v1_Dh5Xjn+yaEnFbJwscTH0sg=="')
# tt.getMe()




