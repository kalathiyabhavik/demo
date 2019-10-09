from django.shortcuts import render, redirect,  get_object_or_404
from .forms import StudentForm,UserSignupForm,StudentFeesForm
from .models import Student ,StudentFees
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='login')
def home(request):
    current_user = request.user.id

    show = Student.objects.filter(user = request.user.id)
    # show = Student.objects.all()
    return render(request, 'home.html', {'show': show})


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
        form = StudentForm(request.POST,  request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
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
    return render(request, 'edit.html', {'form': form})


@login_required(login_url='login')
def delete(request, pk):

    show = Student.objects.get(pk=pk)
    show.delete()
    return redirect('student:home')


@login_required(login_url='login')
def fees(request):
    if request.method == "POST":

        form = StudentFeesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'done')
            return redirect('student:showfees')
    else:

        form = StudentFeesForm()
    return render(request, 'manage_fees.html', {'form': form})


@login_required(login_url='login')
def showfees(request):
    show = StudentFees.objects.all()
    return render(request,'show_fees.html', {'show': show})


@login_required(login_url='login')
def feededit(request, pk):
    instance = get_object_or_404(StudentFees, pk=pk)
    form = StudentFeesForm(request.POST or None, instance=instance, )
    if form.is_valid():
        form.save()
        return redirect('student:showfees')
    return render(request, 'edite.html', {'form': form})


@login_required(login_url='login')
def feesdelete(request, pk):

    show = StudentFees.objects.get(pk=pk)
    show.delete()
    return redirect('student:showfees')
