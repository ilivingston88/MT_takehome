from django.db import models

#fizzbuzz model
class FizzBuzz(models.Model):
    #primary key
    id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=100)
    #auto insert datetime when created
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()