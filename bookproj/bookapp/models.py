from django.db import models
from log_reg_app.models import User

class Book(models.Model):
    title = models.CharField(max_length=55)
    desc = models.TextField()
    created_by = models.ForeignKey(User, related_name="user_created", default="", on_delete=models.CASCADE)
    faved_books = models.ManyToManyField(User, related_name="favorited_books")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)