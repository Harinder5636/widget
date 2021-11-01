
from django.db import models

class Widget(models.Model):
    description = models.TextField(max_length=100)
    quantity = models.IntegerField(default=0)