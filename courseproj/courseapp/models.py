from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name must be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=55)
    desc = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CourseManager()