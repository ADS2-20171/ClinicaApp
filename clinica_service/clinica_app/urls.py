# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf.urls import include, url
#from django.conf import settings
from rest_framework import routers

#from .views import ClienteViewSet
from clinica_app import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'clientes', views.ClienteViewSet)
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
# urlpatterns = patterns(
#'',
#url(r'^', include(router.urls)),
#)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', include('rest_framework.authtoken.views.obtain_auth_token')),
]
