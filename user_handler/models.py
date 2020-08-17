from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class USERS(models.Model):
    user=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    last_login= models.DateTimeField(default=timezone.now)
    otp_validate=models.IntegerField(default=0)
    def __str__(self):
        return self.user