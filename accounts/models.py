from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
# Create your models here.
User=get_user_model()
class UserProfile(models.Model):
    gender_choices=(('Male','Male'),('Female','Female'),('Other','Other'))
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    gender=models.CharField(choices=gender_choices,max_length=500)
    mobile_number=models.CharField(max_length=20)


class Address(models.Model):
    name=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    zipeCode=models.CharField(max_length=20)
    locality=models.CharField(max_length=100)
    streetAddress=models.CharField(max_length=200)
    country=models.CountryField(multiple=False)
