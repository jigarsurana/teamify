from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Person(models.Model):
	email_id = models.EmailField(max_length=80, primary_key=True)
	name = models.CharField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?\d{10,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15)
	google_id = models.CharField(max_length=200, blank=True)
	facebook_id = models.CharField(max_length=200, blank=True)
	gender = models.CharField(max_length=1, blank=True)
	city= models.CharField(max_length=51, blank=True)
