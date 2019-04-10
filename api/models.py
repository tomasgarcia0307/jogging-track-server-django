from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# class User(AbstractUser):
#     name = models.CharField(max_length=100, blank=True, null=True)

class Record(models.Model):
    distance = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)