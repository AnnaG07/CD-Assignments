from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth import logout
from .models import *
import bcrypt

def base(request):
    return render (request, 'login.html')

def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Email/Password")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['name'] = user.first_name
        return redirect('/books')
    return redirect('/')
    
def register(request):
    if request.method == 'POST':
        print(request.POST)
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
        return redirect('/books')
    return redirect('/')

def success(request):
    if 'name' not in request.session:
        return redirect('/')
    return render(request, 'books.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    request.session.clear()
    return redirect('/')



