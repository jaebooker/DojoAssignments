from __future__ import unicode_literals
from django.db import models

#class User(models.Model):
  #first_name = models.CharField(max_length=25)
  #last_name = models.CharField(max_length=25)
  #age = models.IntegerField()
  #created_at = models.DateTimeField(auto_now_add=True)
  #updated_at = models.DateTimeField(auto_now=True)
  #def __str__(self):
    #return self.first_name + " " + self.last_name

class Post(models.Model):
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=2000)
    #user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.TextField(max_length=500)
    #user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
