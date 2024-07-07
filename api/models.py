from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.

class CustomUUIDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('unique', True)
        kwargs.setdefault('default', uuid.uuid4)
        super().__init__(*args, **kwargs)

class UserModel(models.Model):
    # user_id = models.AutoField(primary_key=True)
    securityCode = models.CharField(primary_key=True, editable=False, max_length=255, unique=True)
    # securityCode = CustomUUIDField(primary_key=True, editable=False)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    imageUrl = models.CharField(max_length=500)
    # latitude = models.FloatField()
    # longitude = models.FloatField() 

    def __str__(self):
        return self.name  # + ' -- ' + str(self.securityCode)

class GroupModel(models.Model):
    groupId = CustomUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=500)
    
    # many to many relation
    users = models.ManyToManyField(UserModel, related_name='user')
    
    @property
    def users_count(self):
        return self.users.count()

    # One to many relation
    # users = models.ForeignKey(UserModel,  null = True, blank = True,  on_delete = models.CASCADE, related_name='users')
    
    def __str__(self):
        return self.name # + ' -- ' 

    # idList = ArrayField(    models.CharField(max_length=20))
    # idList = []



from django.contrib import admin

admin.site.register(UserModel)
admin.site.register(GroupModel)