from django.urls import path 
from .views import (
    checkExistAccountFBViews ,
    ProjectListView ,
    AgentListView ,
    AccountLoginInfoListView ,
    )


urlpatterns = [
    path('api/checkExistAccountFBViews',checkExistAccountFBViews) ,
    path("api/projects" , ProjectListView.as_view()) ,
    path("api/agents" , AgentListView.as_view()) ,
    path("api/accounts" , AccountLoginInfoListView.as_view()),
] 

