from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be in valid email format"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['pw_conf']:
            errors['pw_conf'] = "Passwords do not match"
        return errors

    def authenticate(self, email, password):
        user = self.filter(email=email)
        if not user:
            return False
        user = user[0]
        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()