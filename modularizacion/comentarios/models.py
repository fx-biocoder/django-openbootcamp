from typing import Any
from django.db import models

# Create your models here.
class Comment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=100, default="Firma")

    def __str__(self):
        return self.name
    
