from django.db import models

# Create your models here.
class Personel (models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    rutbe = models.CharField(max_length=30)
    age = models.IntegerField()
