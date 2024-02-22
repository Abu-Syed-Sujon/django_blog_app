'this is about model'
from django.db import models

# Create your models here.
class Teacher(models.Model):
    'Teacher information'
    tid= models.IntegerField()
    tname=models.CharField(max_length=40)
    temail=models.EmailField(max_length=30)
    
    #objects = models.Manager()
    