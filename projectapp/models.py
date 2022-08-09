from unicodedata import name
from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)