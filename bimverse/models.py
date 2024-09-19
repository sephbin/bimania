from django.db import models
from .models_utils import *


class edgeObject(parentModel):
    def __str__(self):
        return self.name

class nodeObject(parentModel):
    def __str__(self):
        return self.name