import graphene
from graphene_django import DjangoObjectType

from .models import *

class edgeObject_Type(DjangoObjectType):
    class Meta:
        model = edgeObject
        fields = ("identifier", "name", "enabled", "hasError")

class nodeObject_Type(DjangoObjectType):
    class Meta:
        model = nodeObject
        fields = ("identifier", "name", "enabled", "hasError")

class Query(graphene.ObjectType):
    all_node_objects = graphene.List(nodeObject_Type)
    edges_by_name = graphene.Field(edgeObject_Type, name=graphene.String(required=True))

    def resolve_all_node_objects(root, info):
        # We can easily optimize query count in the resolve method
        # return nodeObject.objects.select_related("edgeObject").all()
        return nodeObject.objects.all()

    def resolve_edges_by_name(root, info, name):
        try:
            return edgeObject.objects.get(name=name)
        except edgeObject.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)