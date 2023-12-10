from django.urls import path ,include
from .views import (
    checkExistAccountFViews ,
    testLogin ,
    )


urlpatterns = [
    path('checkExistAccountFViews',checkExistAccountFViews) ,
    path('testlogin',testLogin)
] 

