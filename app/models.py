from django.db import models
from app.models import *
# Create your models here.
class Country(models.Model):
    Country_Name=models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.Country_Name
    
class Capital(models.Model):
    Country_Name=models.OneToOneField(Country,on_delete=models.CASCADE)
    Capital_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.Capital_Name