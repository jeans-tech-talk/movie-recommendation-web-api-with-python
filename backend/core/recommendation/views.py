from rest_framework import viewsets

from core.recommendation.models import Genre, Movie, Watchlist
from core.recommendation.serializers import GenreSerializer, MovieWriteSerializer, MovieReadSerializer, \
    WatchlistWriteSerializer, WatchlistReadSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.order_by('-id')
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.order_by('-id')
    write_serializer_class = MovieWriteSerializer
    read_serializer_class = MovieReadSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.write_serializer_class


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.order_by('-id')
    write_serializer_class = WatchlistWriteSerializer
    read_serializer_class = WatchlistReadSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.write_serializer_class
