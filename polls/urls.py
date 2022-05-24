# polls/urls.py 

from nturl2path import url2pathname
from django.urls import URLPattern, path 

from . import views 

urlpatterns = [
    path('', views.index, name='index')
]