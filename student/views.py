from django.shortcuts import render, redirect,  get_object_or_404
from .forms import StudentForm
from .models import Student
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms import UserSignupForm
from django.contrib import messages



def home(request):

    show = Student.objects.all()
    return render(request, 'home.html', {'show': show})


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            return redirect('student:login')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})


def login(request):

    if request.method == 'POST':
        username = request.POST['email']
        password1 = request.POST['password']
        user = authenticate(username=username, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect('student:home')
        else:
            messages.warning(request, 'Please correct the error below.')
    return render(request, 'login.html')


def add(request):

    if request.method == 'POST':
        form = StudentForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:home')
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})


def update(request, pk):

    instance = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, request.FILES or None, instance=instance,)
    if form.is_valid():
        form.save()
        return redirect('student:home')
    return render(request,'edit.html' , { 'form': form})


def delete(request, pk):

    show = Student.objects.get(pk = pk)
    show.delete()
    return redirect('student:home')
