from django.db import models

#fizzbuzz model
class FizzBuzz(models.Model):
    #primary key generated automatically upon creation
    id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=100)
    #datetime generated automatically upon creation
    #not necessary to add import datetime to models
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()