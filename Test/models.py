from django.db import models

# Create your models here.

class Random(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True,null=True)

class Queue(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()

from django.contrib import admin
admin.site.register(Random)
admin.site.register(Queue)