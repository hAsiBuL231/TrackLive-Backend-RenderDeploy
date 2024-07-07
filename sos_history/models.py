from django.db import models
from simple_history.models import HistoricalRecords

class SOSHistory(models.Model):
    securityCode = models.CharField(primary_key=True, editable=False, max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # phone_numbers = models.JSONField()  # Store list of phone numbers as JSON
    phone_numbers = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    

from django.contrib import admin
admin.site.register(SOSHistory)