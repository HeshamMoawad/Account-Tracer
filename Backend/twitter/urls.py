from django.urls import path 
from .api.urls import urlpatterns as apiURLS
 

urlpatterns = [

    ## main URLS here
] 

urlpatterns += apiURLS
