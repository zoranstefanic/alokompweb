from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'user/(\w+)$', wp_user, name="wp_user"),
    url(r'$', workplan, name="workplan"),
]
