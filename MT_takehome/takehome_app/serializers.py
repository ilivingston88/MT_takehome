from rest_framework import serializers
from .models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ['id', 'user_agent', 'date_created', 'message']