from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'$', d3, name="d3"),
]
