from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
