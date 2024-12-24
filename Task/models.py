from django.db import models

# Create your models here.

class crud(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    course = models.CharField(max_length=255)
    address = models.TextField()

    

