from django.urls import path 
from .views import home
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    ## main URLS here
    path("",home),
    re_path(r'^$', home),
    re_path(r'^(?:.*)/?$', home),

] 

