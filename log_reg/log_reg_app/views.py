from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
#import bcrypt

def base(request):
    return render (request, 'login.html')

def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if logged_user.password == request.POST['password']:
                request.session['name'] = logged_user.first_name
                return redirect('/success')
    return redirect('/')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        #hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['name'] = new_user.first_name
        return redirect('/success')
    return redirect('/')

def success(request):
    return render(request, 'success.html')

def logout(request):
    request.session.flush()
    return redirect('/')
