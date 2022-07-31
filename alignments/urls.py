from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(\w+)/(\w+)$', alignments, name="alignments"),
]
