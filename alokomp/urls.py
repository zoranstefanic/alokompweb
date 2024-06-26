"""alokomp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^about/', about, name="about"),
    url(r'^ngl/', ngl, name="ngl"),
    url(r'^team/', team, name="team"),
    url(r'^oldnews/', oldnews, name="oldnews"),
    url(r'^gannt/', gannt, name="gannt"),
    url(r'^scheme/', scheme, name="scheme"),
    url(r'^postdoc/', postdoc, name="scheme"),
    url(r'^qscore/',qscore, name="qscore"),
    url(r'^heatmap/',heatmap, name="heatmap"),
    url(r'^equipment/', equipment, name="equipment"),
    url(r'^results/xc', results_xc, name="results_xc"),
    url(r'^results/md', results_md, name="results_md"),
    url(r'^results/ml', results_ml, name="results_ml"),
    url(r'^news/', include("news.urls")),
    url(r'^pdbase/', include("pdbase.urls")),
    url(r'^search/', include("search.urls")),
    url(r'^account/', include("account.urls")),
    url(r'^alignments/', include("alignments.urls")),
    url(r'^md/', include("md.urls")),
    url(r'^msa/', include("msa.urls")),
    url(r'^plots/', include("plots.urls")),
    url(r'^workplan/', include("workplan.urls")),
    url(r'^symmetry/', include("symmetry.urls")),
    url(r'^d3/', include("d3.urls")),
    url(r'^admin/', admin.site.urls),
]
