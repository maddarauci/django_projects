# polls/urls.py 

from nturl2path import url2pathname
from django.urls import URLPattern, path 

from . import views 

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk/', views.DetailView.as_view(), name='detail'),
    path('<int:pk/results', views.ResultsView.as_view(), name='results'),
    path('<int:pk/question_id', views.vote, name='vote'),
]