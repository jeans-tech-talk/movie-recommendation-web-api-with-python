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

    objects = models.Manager()
