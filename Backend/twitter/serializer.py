from .models import (
    # AccountRecord ,
    # TwitterAccount , 
    Agent , 
    Project
    )
from rest_framework.serializers import ModelSerializer



class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['name','imgURL','color']



class AgentSerializer(ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Agent
        fields = ['name','project']

# class TwitterAccountSerializer(ModelSerializer):
#     class Meta:
#         model = TwitterAccount
#         fields = '__all__'


# class AccountRecordSerializer(ModelSerializer):
#     class Meta:
#         model = AccountRecord
#         fields = '__all__'

