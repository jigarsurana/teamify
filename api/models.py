from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class YourSkills(models.Model):
	skill_name = models.CharField(max_length=200)

class YourExpertise(models.Model):
	expertise_name = models.CharField(max_length=200)

class ReqSkills(models.Model):
	skill_name = models.CharField(max_length=200)

class ReqExpertise(models.Model):
	expertise_name = models.CharField(max_length=200)

class Person(models.Model):
	email_id = models.EmailField(max_length=80, primary_key=True)
	name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=15)
	your_skills = models.ManyToManyField(YourSkills)