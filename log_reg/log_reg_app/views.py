from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import *
import bcrypt

def base(request):
    return render (request, 'login.html')

def login(request):
    """
    if request.method == 'POST':
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if logged_user.password == request.POST['password']:
                request.session['name'] = logged_user.first_name
                return redirect('/success')
    return redirect('/')
    """
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode('utf-8'), logged_user.password.encode('utf-8')):
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        password = request.POST['password']
        hashedpw = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        print(hashedpw)
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashedpw)
        request.session['name'] = new_user.first_name
        return redirect('/success')
    return redirect('/')

def success(request):
    if 'name' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    request.session.clear()
    return redirect('/')



