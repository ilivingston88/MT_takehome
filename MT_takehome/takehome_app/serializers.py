from rest_framework import serializers
from .models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        #need to match models fields
        fields = ['id', 'useragent', 'creation_date', 'message']