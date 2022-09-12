from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class Player_form (forms.Form):
    First_name= forms.CharField(max_length=30)
    Second_name= forms.CharField(max_length=30)
    club= forms.CharField(max_length=60)
    shirt_number= forms.IntegerField(max_length=2)
    height= forms.FloatField()
    age= forms.FloatField()

class Coachs_Staff_form (forms.Form):
    first_name= forms.CharField(max_length=30)
    second_name= forms.CharField(max_length=30)
    age= forms.FloatField()
    work_area= forms.CharField(max_length=60)