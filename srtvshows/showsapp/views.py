from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def base(request):
    return render(request, 'shows.html', {"shows": Show.objects.all()})

def view_show(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'show.html', context)

def edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def update(request, id):
    if request.method == 'POST':
        errors = Show.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/edit/{id}')
        else:
            edit_show = Show.objects.get(id=id)
            edit_show.title = request.POST['title']
            edit_show.network = request.POST['network']
            edit_show.release = request.POST['release']
            edit_show.desc = request.POST['desc']
            edit_show.save()
        return redirect(f'/shows/{id}')
    return redirect('/')

def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/')

def new(request):
    return render(request, 'create.html')

def create(request):
    if request.method == 'POST':
        errors = Show.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], desc=request.POST['desc'])
        return redirect('/')
    return redirect('/')



