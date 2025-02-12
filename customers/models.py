from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=64)
    vat_id = models.CharField(max_length=16)
    street = models.CharField(max_length=64)
    city  = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

    
    def __str__(self):
        return self.name
