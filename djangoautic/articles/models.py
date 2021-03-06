""" when you cahnge a model you need to run the two following commands
    python manage.py makemigrations
    python manage.py migrate
"""
from django.db import models
from django.db.models.fields import SlugField
from django.urls.converters import SlugConverter
from django.contrib.auth.models import User

# Create your models here.



class Article(models.Model):  # Different Field Types go to django Documentation
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True) # default pic and field can be empty
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.title 

    def snippet(self):
        return self.body[:50] + " ..."

    