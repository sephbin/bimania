from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.

class geometryObject_serializer(serializers.ModelSerializer):
    geometry = serializers.JSONField()
    class Meta:
        model = geometryObject
        fields = ['id','identifier','name', 'geometry']

class edgeObject_to_serializer(serializers.ModelSerializer):
    class Meta:
        model = edgeObject
        fields = ['name','nodeObject_to']

class edgeObject_from_serializer(serializers.ModelSerializer):
    class Meta:
        model = edgeObject
        fields = ['name','nodeObject_from']

class nodeObject_serializer(serializers.HyperlinkedModelSerializer):
    geometryObjects = geometryObject_serializer(many=True, read_only=True)
    nodeObject_to = edgeObject_to_serializer(source='edgeFrom', many=True, read_only=True)
    nodeObject_from = edgeObject_to_serializer(source='edgeTo', many=True, read_only=True)
    # nodeObject_to = serializers.SlugRelatedField(source='edgeFrom', many=True, read_only=True, slug_field='nodeObject_to.id' )
    # nodeObject_from = serializers.SlugRelatedField(source='edgeTo', many=True, read_only=True, slug_field='nodeObject_from.id' )
    class Meta:
        model = nodeObject
        fields = ['id','name', 'identifier', 'enabled', 'geometryObjects', 'nodeObject_to','nodeObject_from']


class edgeObject_serializer(serializers.ModelSerializer):
    class Meta:
        model = edgeObject
        
        fields = ['id','name', 'identifier', 'enabled', 'nodeObject_from','nodeObject_to']