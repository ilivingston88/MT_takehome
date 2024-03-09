# from django.shortcuts import render #unused
from rest_framework import viewsets
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer

# Create your views here.
class FizzBuzzViewSet(viewsets.ModelViewSet):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer
