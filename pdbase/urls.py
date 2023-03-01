from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', pdbase_home, name="pdbase_home"),
    url(r'proba/$', proba, name="proba"),
    url(r'structures/$', Structures.as_view(), name="structures_list"),
    url(r'structure/(?P<pk>\w+)$', Structure.as_view(), name="structure_view"),
    url(r'structure/ngl/(\w+)$', structure_ngl_view, name="structure_ngl_view"),
    url(r'structure/(\w+)/chains/$', structure_chains, name="structure_chains"),
    url(r'structure/(\w+)/chain/(\w+)$', chain_view, name="chain_view"),
    url(r'structure/(\w+)/chain/(\w+)/-?(\d+)$', residue_view, name="residue_view"),
]
