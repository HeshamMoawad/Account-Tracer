from .models import (AccountRecord , TwitterAccount)
from rest_framework.serializers import ModelSerializer


class TwitterAccountSerializer(ModelSerializer):
    class Meta:
        model = TwitterAccount
        fields = '__all__'




class AccountRecordSerializer(ModelSerializer):
    class Meta:
        model = AccountRecord
        fields = '__all__'

