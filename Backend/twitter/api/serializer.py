from ..models import (
    TwitterAccount,
    Agent,
    Project,
    AccountLoginInfo,
    FollowUnFollow,
    Chat,
    Tweet,
    Reply ,
    MediaLink ,
    FollowExtractor
)
from rest_framework.serializers import ModelSerializer, SerializerMethodField 


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'imgURL', 'color']


class TwitterAccountSerializer(ModelSerializer):
    class Meta:
        model = TwitterAccount
        fields = ['handle']  # ,'password'


class AgentSerializer(ModelSerializer):
    accounts_count = SerializerMethodField()
    project = ProjectSerializer()

    def get_accounts_count(self, obj):
        return TwitterAccount.objects.filter(agent=obj).count()

    class Meta:
        model = Agent
        fields = ['name', 'project', 'accounts_count']


class AccountLoginInfoSerializer(ModelSerializer):
    account = TwitterAccountSerializer()

    class Meta:
        model = AccountLoginInfo
        fields = [
            'name',
            'description',
            'profileImgURL',
            'cookies',
            'token',
            'verified',
            'suspend',
            'account',
            'created_at',
            'created_datetime',
            'updated_datetime',
        ]


class AnalyticsSerializer(ModelSerializer):
    params_as_kwargs = {}
    handle = SerializerMethodField()
    stats = SerializerMethodField()
    messages = SerializerMethodField()
    tweets = SerializerMethodField()
    replies = SerializerMethodField()
    

    def get_handle(self, obj: AccountLoginInfo) -> str:
        return obj.screen_name

    def get_stats(self, obj: AccountLoginInfo):
        followUnfollowObjects = FollowUnFollow \
                .objects \
                    .filter(
                        account=obj.account,
                        **self.params_as_kwargs
                        ) \
                        .order_by('created_datetime')
        print(followUnfollowObjects.first() , followUnfollowObjects.last())
        extractor = FollowExtractor(
            oldObject = followUnfollowObjects.first() ,
            newObject = followUnfollowObjects.last()
        )
        try:    
            return {
                "follow": extractor.get_follow() ,
                "unfollow": extractor.get_unfollow() ,
                "followback": extractor.get_follow_back() ,
            }
        except (IndexError , AttributeError) :
            return {
                "follow": 0,
                "unfollow": 0,
                "followback": 0 ,
            }

    def get_messages(self, obj: AccountLoginInfo):
        return Chat.objects.filter(
            account=obj.account,
            chat_datetime__date = list(self.params_as_kwargs.values())[0] ,
        ).count()

    def get_tweets(self, obj: AccountLoginInfo):
        return Tweet.objects.filter(
            account=obj.account,
            created_at__date=list(self.params_as_kwargs.values())[0],
            **self.params_as_kwargs

        ).count()

    def get_replies(self, obj: AccountLoginInfo):
        return Reply.objects.filter(
            account=obj.account,
            created_at__date=list(self.params_as_kwargs.values())[0],
            **self.params_as_kwargs
        ).count()

    def set_conditions(self,**kwargs):
        """ 
        func to handling date of this analytics 
        to get more spacific resault can pass a kwargs for __init__ and model will pass them to resaults 

            Example :
            >>> serializer = AnalyticsSerializer(instance)
            >>> serializer.set_conditions(
                    created_datetime__range=(
                        datetime(1,12,2023), # start  date
                        datetime(30,12,2023), # end  date
                        ))
            >>> serializer.data
                # that will return all data in this range of date 
         """
        self.params_as_kwargs = kwargs

    class Meta:
        model = AccountLoginInfo
        fields = [
            'name',
            'handle',
            'stats',
            'messages',
            'profileImgURL',
            'tweets',
            'replies',
        ]

class MediaLinksSerializer(ModelSerializer):
    class Meta:
        model = MediaLink
        fields = '__all__'


class TweetSerializer(ModelSerializer):
    media_links = MediaLinksSerializer(many=True,read_only=True)
    class Meta:
        model = Tweet
        fields = [
            "conversation_id_str",
            'favorite_count',
            'reply_count',
            'retweet_count',
            'user_id_str',
            'bookmark_count',
            'full_text',
            'created_at',
            "media_links",
            "retweted_from",
            "quoted_retweted_from"
        ]
        depth = 1

class ReplySerializer(ModelSerializer):
    media_links = MediaLinksSerializer(many=True,read_only=True)
    class Meta:
        model = Reply
        fields = [
            "conversation_id_str",
            "in_reply_to_screen_name",
            'favorite_count',
            'reply_count',
            'retweet_count',
            'user_id_str',
            'bookmark_count',
            'full_text',
            'created_at',
            "media_links",
            "replied_from",
        ]
        depth = 1
