from django.shortcuts import render, redirect,  get_object_or_404
from .forms import StudentForm
from .models import Student
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    current_user = request.user.id

    show = Student.objects.filter(user = request.user.id)
    return render(request, 'home.html', {'show': show , 'name': current_user})


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('student:login')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         password1 = request.POST['password']
#         user = authenticate(request, username=username, password=password1)
#         if user is not None:
#             login(request, user)
#             return redirect('student:home')
#         else:
#             messages.warning(request, 'Please correct the error below.')
#     return render(request, 'login.html')

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.user = request.user.id
            form.save()
            return redirect('student:home')
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})

@login_required(login_url='login')
def update(request, pk):
    instance = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, request.FILES or None, instance=instance,)
    if form.is_valid():
        form.save()
        return redirect('student:home')
    return render(request,'edit.html' , { 'form': form})

@login_required(login_url='login')
def delete(request, pk):

    show = Student.objects.get(pk = pk)
    show.delete()
    return redirect('student:home')
