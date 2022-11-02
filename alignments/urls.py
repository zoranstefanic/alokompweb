from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(\w+)/(\w+)$', alignment1, name="alignment1"),
    url(r'alignment/(\w+)/(\w+)/(\w+)/(\w+)/$', alignment, name="alignment"),
    url(r'list/$', AlignmentsList.as_view(), name="alignments_list"),
]
