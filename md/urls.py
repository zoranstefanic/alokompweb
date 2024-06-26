from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'directories/$', MDdirectoriesView.as_view(), name="MDdirectoriesView"),
    url(r'trajectories/$', MDtrajectoriesView.as_view(), name="MDtrajectoriesView"),
    url(r'trajectories/analyzed/$', MDAnalyzedView.as_view(), name="MDAnalyzedView"),
    url(r'trajectories/replica/(\d)$', replica, name="replica"),
    url(r'directory/(?P<pk>\d+)$', MDdirectoryView.as_view(), name="MDdirectoryView"),
    url(r'trajectory/(?P<pk>\d+)$', MDtrajectoryView.as_view(), name="MDtrajectoryView"),
    url(r'cm/(?P<pk>\d+)$',CorrelationMatrixView.as_view(), name="CorrelationMatrixView"),
    url(r'ramachandran/(?P<pk>\d+)/(?P<num>\d+)$', ramachandran, name="ramachandran"),
    url(r'correlations/(?P<pk>\d+)/(?P<num>\d+)$', correlations, name="correlations"),
    url(r'correlations/traj/(?P<pk>\d+)/$', correlations_for_traj, name="correlations_for_traj"),
    url(r'correlations_old/(?P<pk>\d+)/(?P<num>\d+)$', correlations_old, name="correlations_old"),
    url(r'correlations_circular/(?P<pk>\d+)/(?P<num>\d+)$', correlations_circular, name="correlations_circular"),
    url(r'correlations_highest/(?P<pk>\d+)/(?P<num>\d+)$', correlations_highest, name="correlations_highest"),
    url(r'avocados/(?P<pk>\d+)/(?P<chain>\w)$', avocados, name="avocados"),
    url(r'overlap/(?P<pk>\d+)/(?P<num1>\d+)/(?P<num2>\d+)$', overlap, name="overlap"),
    url(r'ramachandran/replicas/(?P<trid>\d+)/(?P<resid>\d+)$', residue_in_replicas, name="residue_in_replicas"),
    url(r'ramachandran/residue_in_all/(?P<trid>\d+)/(?P<resid>\d+)$', residue_in_all, name="residue_in_all"),
    url(r'trajectory/ta/(\d+)$', torsion_plot, name="torsion_plot"),
    url(r'trajectory/changepoints/(\d+)$', changepoints_plot, name="changepoints_plot"),
    url(r'trajectory/graph/(\d+)$', graph_plot, name="graph_plot"),
]
