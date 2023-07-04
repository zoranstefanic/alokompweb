from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'directories/$', MDdirectoriesView.as_view(), name="MDdirectoriesView"),
    url(r'trajectories/$', MDtrajectoriesView.as_view(), name="MDtrajectoriesView"),
    url(r'trajectories/analyzed/$', MDAnalyzedView.as_view(), name="MDAnalyzedView"),
    url(r'trajectories/replica/(\d)$', replica, name="replica"),
    url(r'directory/(?P<pk>\d+)$', MDdirectoryView.as_view(), name="MDdirectoryView"),
    url(r'trajectory/(?P<pk>\d+)$', MDtrajectoryView.as_view(), name="MDtrajectoryView"),
    url(r'ramachandran/(?P<pk>\d+)/(?P<num>\d+)$', ramachandran, name="ramachandran"),
    url(r'correlations/(?P<pk>\d+)/(?P<num>\d+)$', correlations, name="correlations"),
    url(r'overlap/(?P<pk>\d+)/(?P<num1>\d+)/(?P<num2>\d+)$', overlap, name="overlap"),
    url(r'ramachandran/replicas/(?P<trid>\d+)/(?P<resid>\d+)$', residue_in_replicas, name="residue_in_replicas"),
    url(r'trajectory/ta/(\d+)$', torsion_plot, name="torsion_plot"),
]
