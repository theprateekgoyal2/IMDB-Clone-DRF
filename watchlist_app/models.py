from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=50, blank=True)
    platform = models.ManyToManyField(StreamingPlatform, blank=True)
    storyline = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    total_ratings = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    movie = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="Reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rating} | {self.movie.title} | {self.reviewer}'