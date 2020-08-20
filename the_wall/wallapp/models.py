from django.db import models
from log_reg_app.models import User

class Wall_Message(models.Model):
    m_content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="poster_message", default="", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Wall_Comment(models.Model):
    c_content = models.CharField(max_length=255)
    message = models.ForeignKey(Wall_Message, related_name="comment_message", default="", on_delete=models.CASCADE)
    poster = models.ForeignKey(User, related_name="poster_comment", default="", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)