from __future__ import unicode_literals
from django.db import models
class Course(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
