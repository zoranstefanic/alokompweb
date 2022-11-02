from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(?P<pk>\d+)/$', MSAalignmentView.as_view(), name="msa"),
]
