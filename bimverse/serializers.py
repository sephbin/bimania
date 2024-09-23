from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.

class geometryObject_serializer(serializers.ModelSerializer):
    geometry = serializers.JSONField()
    class Meta:
        model = geometryObject
        fields = ['id','identifier','name', 'geometry']

class nodeObject_serializer(serializers.HyperlinkedModelSerializer):
    geometryObjects = geometryObject_serializer(many=True, read_only=True)
    class Meta:
        model = nodeObject
        fields = ['id','name', 'identifier', 'enabled', 'geometryObjects',]


class edgeObject_serializer(serializers.ModelSerializer):
    class Meta:
        model = edgeObject
        
        fields = ['id','name', 'identifier', 'enabled', 'nodeObject_from','nodeObject_to']