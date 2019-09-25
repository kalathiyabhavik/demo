from django.shortcuts import render, redirect,  get_object_or_404
from .forms import StudentForm
from .models import Student


def home(request):
    show = Student.objects.all()
    return render(request, 'home.html', {'show': show})


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
