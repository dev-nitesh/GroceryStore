from django.db import models
from datetime import datetime
# Create your models here.
class DeliveryPartner(models.Model):

    name = models.CharField(max_length=100)
    photo = models.ImageField('photos/%Y/%m%d/')
    address = models.TextField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=20, blank=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    aadharNumber = models.IntegerField()
    aadharImage = models.ImageField('photos/%Y/%m%d/')
    licenseNumber = models.IntegerField()
    ServicableAreaMin = models.IntegerField()
    ServicableAreaMax = models.IntegerField()
    is_loyal = models.BooleanField(default=True)
    deliveryStatus = models.CharField(max_length=50, blank=True)
    hire_date= models.DateTimeField(default= datetime.now, blank=True)
    def __str__(self):
        return self.name