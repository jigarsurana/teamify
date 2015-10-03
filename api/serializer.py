from rest_framework import serializers
# from django.forms import widgets
from api.models import *

class YourSkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = YourSkills
		fields = ("skill_name")

class PersonSerializer(serializers.ModelSerializer):
    your_skills = YourSkillSerializer(many= True, required = False)
    class Meta:
        model = Person
        fields = ('email_id', 'name', 'phone_number', 'your_skills')