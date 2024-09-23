from django.urls import path, include
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

# ViewSets define the view behavior.
class nodeObject_viewSet(viewsets.ModelViewSet):
    queryset = nodeObject.objects.all()
    serializer_class = nodeObject_serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter , DjangoFilterBackend, ]
    filterset_fields = {'updated':['gte', 'lte', 'exact', 'gt', 'lt'], 'created':['gte', 'lte', 'exact', 'gt', 'lt']}
    search_fields = ('$name','$identifier',)
    ordering_fields = '__all__'
    ordering = ['createdBy','pk',]

class edgeObject_viewSet(viewsets.ModelViewSet):
    queryset = edgeObject.objects.all()
    serializer_class = edgeObject_serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter , DjangoFilterBackend, ]
    filterset_fields = {'updated':['gte', 'lte', 'exact', 'gt', 'lt'], 'created':['gte', 'lte', 'exact', 'gt', 'lt']}
    search_fields = ('$name','$identifier',)
    ordering_fields = '__all__'
    ordering = ['createdBy','pk',]

class geometryObject_viewSet(viewsets.ModelViewSet):
    queryset = geometryObject.objects.all()
    serializer_class = geometryObject_serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter , DjangoFilterBackend, ]
    filterset_fields = {'updated':['gte', 'lte', 'exact', 'gt', 'lt'], 'created':['gte', 'lte', 'exact', 'gt', 'lt']}
    search_fields = ('$name','$identifier',)
    ordering_fields = '__all__'
    ordering = ['createdBy','pk',]