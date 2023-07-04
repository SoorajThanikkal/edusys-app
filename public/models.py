from django.db import models

# Create your models here.
class register(models.Model):
    firstname=models.CharField(max_length=100,default='')
    lastname=models.CharField(max_length=100,default='')
    Gmail=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    Gender=models.CharField(max_length=100,default='')
    usertype=models.CharField(max_length=100,default='')
