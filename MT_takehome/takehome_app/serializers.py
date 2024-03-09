import rest_framework import serializers
from .models import FizBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ['id', 'user_agent', 'date_created', 'message']