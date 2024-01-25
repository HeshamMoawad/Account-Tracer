from django.urls import path 
from .api.urls import urlpatterns as apiURLS
from .views import home
from django.urls import path, re_path

urlpatterns = [
    
]


urlpatterns += apiURLS

urlpatterns += [
    ## main URLS here

] 
