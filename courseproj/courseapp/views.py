from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def base(request):
    return render(request, 'courses.html', {"courses": Course.objects.all()})

def create(request):
    if request.method == 'POST':
        errors = Course.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        print(course)
    return redirect('/')

def destroy(request, id):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request, 'destroy.html', context)
    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('/')
