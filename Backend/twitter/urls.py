from django.urls import path ,include
from .views import (
    checkExistAccountFBViews ,
    testLogin ,
    ProjectListView ,
    AgentListView ,
    )


urlpatterns = [
    path('api/checkExistAccountFBViews',checkExistAccountFBViews) ,
    path('api/testlogin',testLogin),
    path("api/projects" , ProjectListView.as_view()) ,
    path("api/agents" , AgentListView.as_view()) ,
] 

