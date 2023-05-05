from rest_framework import serializers

from core.authentication.serializers import UserWatchlistReadSerializer, UserReviewMovieReadSerializer
from core.recommendation.models import Genre, Movie, Watchlist, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
    )

    class Meta:
        model = Movie
        fields = '__all__'


class MovieWatchlistReadSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ['users']


class WatchlistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['movie']

    def create(self, validated_data):
        request = self.context.get('request')
        return Watchlist.objects.create(
            user=request.user,
            movie=validated_data.get('movie'),
        )


class WatchlistReadSerializer(serializers.ModelSerializer):
    user = UserWatchlistReadSerializer()
    movie = MovieWatchlistReadSerializer()

    class Meta:
        model = Watchlist
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        return Review.objects.create(
            user=request.user,
            **validated_data,
        )


class ReviewMovieReadSerializer(serializers.ModelSerializer):
    user = UserReviewMovieReadSerializer()

    class Meta:
        model = Review
        exclude = ['movie']


class MovieReadSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    reviews = ReviewMovieReadSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ['users']
