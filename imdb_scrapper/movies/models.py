from django.db import models

class Movie(models.Model):
    title = models.TextField()
    image_url = models.TextField()
    page_url = models.TextField()
    mpaa = models.TextField()
    genre = models.TextField()
    year = models.IntegerField()
    rating = models.DecimalField(max_digits = 3, decimal_places = 2)
    director = models.TextField()
