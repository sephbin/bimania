from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.

class geometryObject_serializer(serializers.ModelSerializer):
    geometry = serializers.JSONField()
    class Meta:
        model = geometryObject
        fields = ['name', 'geometry']

class nodeObject_serializer(serializers.HyperlinkedModelSerializer):
    geometryObjects = geometryObject_serializer(many=True, read_only=True)
    class Meta:
        model = nodeObject
        fields = ['name', 'identifier', 'enabled', 'geometryObjects',]


# ViewSets define the view behavior.
class nodeObject_viewSet(viewsets.ModelViewSet):
    queryset = nodeObject.objects.all()
    serializer_class = nodeObject_serializer