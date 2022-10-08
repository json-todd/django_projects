from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length = 100)

class Auto(models.Model):
    nickname = models.CharField(max_length = 100)
    mileage = models.IntegerField()
    comments = models.CharField(max_length = 500)
    make = models.ForeignKey(Make, on_delete = models.CASCADE)
