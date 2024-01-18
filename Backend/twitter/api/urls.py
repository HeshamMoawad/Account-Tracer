from django.urls import path 
from .views import (
    ProjectListView ,
    AgentListView ,
    AccountLoginInfoListView ,
    analyticsFBViews ,
    checkExistHandleFBViews,
    checkExistAccountFBViews ,
    TweetListView ,
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
    path("api/testing",testing),
] 

