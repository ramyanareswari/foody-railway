# Create your models here.
from django.db import models

class Information(models.Model):
    title = models.CharField(max_length=130, null=True,blank=True)
    description = models.TextField(null=True,blank=True)