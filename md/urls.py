from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'directories/$', MDdirectoriesView.as_view(), name="MDdirectoriesView"),
    url(r'trajectories/$', MDtrajectoriesView.as_view(), name="MDtrajectoriesView"),
    url(r'trajectories/torsions/$', MDwithTorsionsView.as_view(), name="MDwithTorsionsView"),
    url(r'trajectories/replica/(\d)$', replica, name="replica"),
    url(r'directory/(?P<pk>\d+)$', MDdirectoryView.as_view(), name="MDdirectoryView"),
    url(r'trajectory/(?P<pk>\d+)$', MDtrajectoryView.as_view(), name="MDtrajectoryView"),
    url(r'trajectory/ta/(\d+)$', torsion_plot, name="torsion_plot"),
]
