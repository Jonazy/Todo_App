from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
