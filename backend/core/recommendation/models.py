from django.contrib.auth import get_user_model
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)

    objects = models.Manager()


class Movie(models.Model):
    title = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField(
        'recommendation.Genre',
        related_name='movies',
    )
    users = models.ManyToManyField(
        get_user_model(),
        related_name='movies',
        through='recommendation.Review',
        blank=True,
    )

    objects = models.Manager()


class Watchlist(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='watchlists',
    )
    movie = models.ForeignKey(
        'recommendation.Movie',
        on_delete=models.CASCADE,
        related_name='watchlists',
    )
    date_added = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()


class Review(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    movie = models.ForeignKey(
        'recommendation.Movie',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
    )
    text = models.TextField()

    objects = models.Manager()
