from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Send_FoodWaste_Model(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)
    address = models.TextField()
    food_type = models.CharField(max_length = 50)
    expiry_date = models.DateField()
    weight = models.IntegerField()