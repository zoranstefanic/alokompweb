from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'gallery/$', symmetry_gallery, name="symmetry_gallery"),
    url(r'd3/(\w+)/$', d3_projections, name="d3_projections"),
    url(r'symmetry/(\w+)/$', structure_symmetry, name="structure_symmetry"),
    url(r'd3_json/(\w+)/$', d3_json, name="d3_json"),
]
