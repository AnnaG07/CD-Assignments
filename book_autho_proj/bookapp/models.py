from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=55)
    desc = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    notes = models.TextField(default='')
    books = models.ManyToManyField(Book, related_name='authors')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)