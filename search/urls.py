from django.conf.urls import *
from .views import *

urlpatterns = [
    url(r"^$", search, name="search"),
]
