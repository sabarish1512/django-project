from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    manufacturer=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    
class Employee(models.Model):
    eid=models.CharField(max_length=30)
    ename=models.CharField(max_length=30)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)

    