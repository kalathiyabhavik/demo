from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
