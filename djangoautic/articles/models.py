""" when you cahnge a model you need to run the two following commands
    python manage.py makemigrations
    python manage.py migrate
"""
from django.db import models
from django.db.models.fields import SlugField
from django.urls.converters import SlugConverter

# Create your models here.



class Article(models.Model):  # Different Field Types go to django Documentation
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # add in thumbnail later
    # add in author later
