from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','image_url','page_url','mpaa','genre','year','rating','director')
