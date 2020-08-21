from django.shortcuts import render, redirect
from .models import *
from log_reg_app.models import *

def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_books': Book.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books.html', context)

def add_book(request):
    if request.method == 'POST':
        print(request.POST)
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], created_by=User.objects.get(id=request.session['user_id']))
        user.favorited_books.add(book)
        return redirect('/books')

def delete(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books')

def view(request, id):
    context = {
        'one_book': Book.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'view.html', context)

def favorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    user.favorited_books.add(book)
    return redirect('/books')

def unfavorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    user.favorited_books.remove(book)
    return redirect('/books')