from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    adult = models.BooleanField()    
    backdrop_path = models.CharField(max_length=200)   
    released_date = models.DateField()
    original_language = models.CharField(max_length=100)
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name='movies')
    
class Actor(models.Model):
    movie_id = models.IntegerField()
    actor_id = models.IntegerField()
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True) 
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_path = models.ImageField(null=True)