from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=55)
    release = models.DateField()
    desc = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ShowManager()