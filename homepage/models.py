from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()