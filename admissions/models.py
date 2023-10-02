from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=1000)
    fathername=models.CharField(max_length=1000)
    classname=models.IntegerField()
    contact=models.CharField(max_length=1000)
