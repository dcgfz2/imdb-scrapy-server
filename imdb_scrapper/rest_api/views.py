from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MovieSerializer
from movies.models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
