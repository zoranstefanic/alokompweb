from django.conf.urls import url
from .views import *
from django.urls import include, path

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<slug:slug>/', NewsItemDetail.as_view(), name='news-item'),
]
