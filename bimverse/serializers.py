from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.

class geometryObject_serializer(serializers.ModelSerializer):
    geometry = serializers.JSONField()
    class Meta:
        model = geometryObject
        fields = ['id','name','geometry','parentObject']

class geometryObjectNested_serializer(serializers.ModelSerializer):
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
    geometryObjects = geometryObjectNested_serializer(many=True, read_only=True)
    nodeObject_to = edgeObject_to_serializer(source='edgeFrom', many=True, read_only=True)
    nodeObject_from = edgeObject_from_serializer(source='edgeTo', many=True, read_only=True)
    #modularClassTags = serializers.SlugRelatedField(many=True, slug_field='name')
    modularClassTags = serializers.StringRelatedField(many=True)
    data = serializers.JSONField()
    # nodeObject_to = serializers.SlugRelatedField(source='edgeFrom', many=True, read_only=True, slug_field='nodeObject_to.id' )
    # nodeObject_from = serializers.SlugRelatedField(source='edgeTo', many=True, read_only=True, slug_field='nodeObject_from.id' )
    class Meta:
        model = nodeObject
        fields = ['id','name', 'identifier', 'enabled', 'data', 'modularClassTags','geometryObjects', 'nodeObject_to','nodeObject_from']

class nodeObject__light_serializer(serializers.HyperlinkedModelSerializer):
    nodeObject_to = edgeObject_to_serializer(source='edgeFrom', many=True, read_only=True)
    nodeObject_from = edgeObject_from_serializer(source='edgeTo', many=True, read_only=True)
    modularClassTags = serializers.StringRelatedField(many=True)
    data = serializers.JSONField()
    # nodeObject_to = serializers.SlugRelatedField(source='edgeFrom', many=True, read_only=True, slug_field='nodeObject_to.id' )
    # nodeObject_from = serializers.SlugRelatedField(source='edgeTo', many=True, read_only=True, slug_field='nodeObject_from.id' )
    class Meta:
        model = nodeObject
        fields = ['id','name', 'identifier', 'enabled', 'data', 'modularClassTags','geometryObjects', 'nodeObject_to','nodeObject_from']


class edgeObject_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = edgeObject
        
        fields = ['id','name', 'identifier', 'enabled', 'nodeObject_from','nodeObject_to']

class modularClassTag_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modularClassTag
        
        fields = ['id','name']