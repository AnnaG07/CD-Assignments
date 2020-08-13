from django.shortcuts import render, redirect
from .models import *

def base(request):
    return render(request, 'home.html', {"books": Book.objects.all()})

def create_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/books')

def view_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(id=id)
    }
    return render(request, 'book.html', context)

def assign_book(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['id'])
    author.books.add(book)
    return redirect(f'/books/{id}')

def create_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def view_author(request, id):
    author = Author.objects.get(id=id)
    context = {
        "author": author,
        "books": Book.objects.exclude(id=id)
    }
    return render(request, 'author.html', context)

def assign_author(request, id):
    author = Author.objects.get(id=id)
    book = Book.objects.get(id=request.POST['id'])
    book.authors.add(author)
    return redirect(f'/authors/{id}')

def authors(request):
    return render(request, 'authors.html', {"authors": Author.objects.all()})

def books(request):
    return render(request, 'books.html', {"books": Book.objects.all()})