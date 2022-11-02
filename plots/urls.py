from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'bokeh/$', bokeh_plot, name="bokeh_plot"),
    url(r'rmsd/$', plot_rmsd, name="plot_rmsd"),
    url(r'qscore/$', plot_qscore, name="plot_qscore"),
]
