from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'gallery/$', symmetry_gallery, name="symmetry_gallery"),
    url(r'(\w+)/$', structure_symmetry, name="structure_symmetry"),
]
