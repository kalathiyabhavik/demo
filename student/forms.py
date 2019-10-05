from django import forms
from .models import Student,StudentFees
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname','lname','email','image','address']


class UserSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class StudentFeesForm(forms.ModelForm):
    class Meta:
        model = StudentFees
        fields = ['date','from_date','to_date','amount','comment','student  ']
