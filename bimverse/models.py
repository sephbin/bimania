from django.db import models
from .models_utils import *

class edgeObject(parentModel):
	project = 					models.CharField(max_length=256, default="--none--")
	nodeObject_from =       models.ForeignKey('nodeObject', on_delete=models.CASCADE, related_name='edgeFrom')
	nodeObject_to =         models.ForeignKey('nodeObject', on_delete=models.CASCADE, related_name='edgeTo')
	def __str__(self):
		return self.name

class nodeObject(parentModel):
	project = 					models.CharField(max_length=256, default="--none--")
	connectedNodeObjects =      models.ManyToManyField('self', through='edgeObject', through_fields=('nodeObject_from', 'nodeObject_to'), symmetrical=False)
	modularClassTags =          models.ManyToManyField('modularClassTag', blank=True, null=True, related_name="nodeObjects")
	dictionary =             	models.JSONField(default={"default":"dictionary"})
	def __str__(self):
		return self.name

class geometryObject(parentModel):
	parentObject =  models.ForeignKey(nodeObject, on_delete=models.CASCADE, related_name="geometryObjects")
	
	# geometry =      DataField()
	def __str__(self):
		return self.name

class modularClassTag(models.Model):
	name =                      models.CharField(max_length=256, unique=True)
	def __str__(self):
		return self.name