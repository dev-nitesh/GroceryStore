from django.db import models

# Create your models here.
class StoreOTPVerificationLinks(models.Model):
    OTP=models.TextField()
    mobileNo=models.CharField(max_length=10)
    uid=models.TextField()