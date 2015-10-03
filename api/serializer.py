from rest_framework import serializers
# from django.forms import widgets
from api.models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('email_id', 'name', 'city','phone_number')
