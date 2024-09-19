from django.db import models
from .models_utils import *


class Category(parentModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(parentModel):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name