from django.db import models

# Create your models here.
class Shoes(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=255)
    price=models.FloatField()
    color=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
class Clothes(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=255)
    price=models.FloatField()
    color=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    
    