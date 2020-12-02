from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=1000)
    number = models.IntegerField()
    def __str__(self):
        return self.name 