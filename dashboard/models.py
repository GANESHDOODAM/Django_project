from django.db import models
from django.forms import CharField

# Create your models here.
class navbar(models.Model):
    name=CharField(max_length=100)