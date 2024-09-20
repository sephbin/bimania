from django.db import models
from .models_utils import *


class edgeObject(parentModel):
    nodeObject_from =       models.ForeignKey('nodeObject', on_delete=models.CASCADE, related_name='edgeFrom')
    nodeObject_to =         models.ForeignKey('nodeObject', on_delete=models.CASCADE, related_name='edgeTo')
    def __str__(self):
        return self.name

class nodeObject(parentModel):
    connectedNodeObjects = models.ManyToManyField('self', through='edgeObject', through_fields=('nodeObject_from', 'nodeObject_to'), symmetrical=False)
    def __str__(self):
        return self.name

class geometryObject(parentModel):
    parentObject =  models.ForeignKey(nodeObject, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related")
    # geometry =      DataField()
    def __str__(self):
        return self.name