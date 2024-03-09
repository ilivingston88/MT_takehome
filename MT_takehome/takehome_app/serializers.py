from rest_framework import serializers
from .models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ['id', 'useragent', 'creation_date', 'message']