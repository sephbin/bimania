from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
from .serializers import *
from .rest_urls import *



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'nodes', nodeObject_viewSet)
router.register(r'edges', edgeObject_viewSet)
router.register(r'geometries', geometryObject_viewSet)
router.register(r'nodes-light', nodeObject_light_viewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]