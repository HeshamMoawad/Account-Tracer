from django.urls import path 
from .views import (
    # List Views
    ProjectListView ,
    AgentListView ,
    AccountLoginInfoListView ,
    TweetListView ,
    ReplyListView ,
    # FB Views
    analyticsFBViews ,
    checkExistHandleFBViews,
    checkExistAccountFBViews ,
    testing
    )


urlpatterns = [
    # API endpoints
    path('api/checkExistAccountFBViews',checkExistAccountFBViews) ,
    path("api/projects" , ProjectListView.as_view()) ,
    path("api/agents" , AgentListView.as_view()) ,
    path("api/accounts" , AccountLoginInfoListView.as_view()),
    path("api/analytics",analyticsFBViews),
    path("api/checkExistHandleFBViews",checkExistHandleFBViews),
    path("api/accountTweets",TweetListView.as_view()) ,
    path("api/accountReplies",ReplyListView.as_view()) ,
    path("api/testing",testing),
] 

