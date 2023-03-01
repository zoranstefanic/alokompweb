from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'position/(?P<pk>\d+)/$', MSApositionView.as_view(), name="msa_position"),
    url(r'(?P<pk>\d+)/$', MSAalignmentView.as_view(), name="msa"),
]
