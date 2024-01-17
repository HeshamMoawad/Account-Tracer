from django.contrib import admin
from .models import (
    TwitterAccount ,
    Project ,
    Agent ,
    AccountLoginInfo ,
    Tweet ,
    Chat ,
    Reply ,
    FollowUnFollow,
    MediaLink ,
    TelegramBotUser
    )

# Register your models here.

admin.site.register(Project)
admin.site.register(Agent)
admin.site.register(TwitterAccount)
admin.site.register(AccountLoginInfo)
admin.site.register(Tweet)
admin.site.register(Chat)
admin.site.register(Reply)
admin.site.register(FollowUnFollow)
admin.site.register(MediaLink)
admin.site.register(TelegramBotUser)


