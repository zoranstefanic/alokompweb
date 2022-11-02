from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'directories/$', MDdirectoriesView.as_view(), name="MDdirectoriesView"),
    url(r'trajectories/$', MDtrajectoriesView.as_view(), name="MDtrajectoriesView"),
    url(r'directory/(?P<pk>\d+)$', MDdirectoryView.as_view(), name="MDdirectoryView"),
    url(r'trajectory/(?P<pk>\d+)$', MDtrajectoryView.as_view(), name="MDtrajectoryView"),
]
