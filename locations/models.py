from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class LocationModel(models.Model):
    securityCode = models.CharField(primary_key=True, editable=False, max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    taker = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)
    latitude = models.FloatField()
    longitude = models.FloatField()
    history = HistoricalRecords()

    def __str__(self): 
        return self.taker 

from django.contrib import admin
admin.site.register(LocationModel)