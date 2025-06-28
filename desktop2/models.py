from django.db import models

# Create your models here.
class Carlist(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    active = models.BooleanField(default=False)