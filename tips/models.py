from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class TipsArticle(models.Model):
    # == if author is deleted, delete objects (not class) related to author as well ==
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.DateTimeField(null=True, blank=True, default=datetime.now)
    image =  models.CharField(max_length=500)

    # string representation method
    def __str__(self):
        return self.title