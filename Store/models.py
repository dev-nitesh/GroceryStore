from django.db import models
from datetime import datetime
# Create your models here.
class Store(models.Model):        
    StoreName = models.CharField(max_length=100)
    StoreAddress = models.TextField(max_length=100)
    OwnerName = models.CharField(max_length=100)
    OwnerNumber = models.IntegerField()
    Email = models.CharField(max_length=50)
    Lat = models.CharField(max_length=100, blank=True)
    Long = models.CharField(max_length=100, blank=True)
    StoreImage = models.ImageField('photos/%Y/%m%d/')
    IsVerified = models.BooleanField(default=True)
    IsPublished = models.BooleanField(default=True)
    ListingDate = models.DateTimeField(default= datetime.now, blank=True)
    IsKYCVerified = models.BooleanField(default=True)
    def __str__(self):
        return self.StoreName 