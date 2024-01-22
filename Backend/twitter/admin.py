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
class ChatAdmin(admin.ModelAdmin):
    list_filter = ( "chat_datetime" , "account")

class TweetsAdmin(admin.ModelAdmin):
    list_filter = ( "account" , "created_at")

class RepliesAdmin(admin.ModelAdmin):
    list_filter = ( "account" , "created_at")

class FollowUnFollowAdmin(admin.ModelAdmin):
    list_filter = ( "account" , "created_datetime")

admin.site.register(Project)
admin.site.register(Agent)
admin.site.register(TwitterAccount)
admin.site.register(AccountLoginInfo)
admin.site.register(Tweet , TweetsAdmin )
admin.site.register(Chat , ChatAdmin)
admin.site.register(Reply , RepliesAdmin)
admin.site.register(FollowUnFollow , FollowUnFollowAdmin)
admin.site.register(MediaLink)
admin.site.register(TelegramBotUser)


