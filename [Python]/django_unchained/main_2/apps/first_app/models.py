# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
class Email(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    #objects = UserManager()
    # *************************
