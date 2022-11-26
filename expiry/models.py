from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food_Data(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    food_name = models.CharField(max_length = 100) # smaller than textfield
    food_expired_date = models.DateField()