from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'directories/$', MDdirectories.as_view(), name="MDdirectories"),
    url(r'directory/(?P<pk>\d+)$', MDdirectory.as_view(), name="MDdirectory"),
    url(r'trajectory/(?P<pk>\d+)$', Trajectory.as_view(), name="Trajectory"),
]
