from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'gallery/$', symmetry_gallery, name="symmetry_gallery"),
    url(r'symmops/$', symmops, name="symmops"),
    url(r'symmop/(\d+)/$', symmop, name="symmop"),
    url(r'residue_symmop_view/(\d+)/$', residue_symmop_view, name="residue_symmop_view"),
    url(r'd3/(\w+)/$', d3_projections, name="d3_projections"),
    url(r'symmetry/(\w+)/$', structure_symmetry, name="structure_symmetry"),
    url(r'space_groups/(\d+)/$', space_groups, name="space_groups"),
    url(r'd3_json/(\w+)/$', d3_json, name="d3_json"),
]
