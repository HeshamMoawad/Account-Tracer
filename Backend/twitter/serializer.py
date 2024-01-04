from .models import (
    TwitterAccount,
    Agent,
    Project,
    AccountLoginInfo,
    FollowUnFollow,
    Chat,
    Tweet,
    Reply
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
        try:
            return {
                "follow":  followUnfollowObjects.last().following - followUnfollowObjects[0].following,
                "unfollow": followUnfollowObjects[0].followers - followUnfollowObjects.last().followers ,
                "followback": followUnfollowObjects.last().followers - followUnfollowObjects[0].followers ,
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
        ).count()

    def get_tweets(self, obj: AccountLoginInfo):
        return Tweet.objects.filter(
            account=obj.account,
            **self.params_as_kwargs

        ).count()

    def get_replies(self, obj: AccountLoginInfo):
        return Reply.objects.filter(
            account=obj.account,
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
