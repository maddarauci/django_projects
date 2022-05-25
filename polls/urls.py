# polls/urls.py 

from nturl2path import url2pathname
from termios import VDISCARD
from django.urls import URLPattern, path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]