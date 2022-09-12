from django.db import models 

class Players (models.Model):
    First_name= models.CharField(max_length=30)
    Second_name= models.CharField(max_length=30)
    club= models.CharField(max_length=60)
    shirt_number= models.IntegerField(max_length=2)
    height= models.FloatField()
    age= models.FloatField()

class Coachs_Staff (models.Model):
    first_name= models.CharField(max_length=30)
    second_name= models.CharField(max_length=30)
    age= models.FloatField()
    work_area= models.CharField(max_length=60)




# Create your models here.
