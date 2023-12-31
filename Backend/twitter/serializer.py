from .models import (
    TwitterAccount,
    Agent,
    Project,
    AccountLoginInfo
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
            'id_str',
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
            'updated_datetime' ,
            ]
