from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.fname +" "+ self.lname


class StudentFees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.student.fname + ' ' + self.student.lname
