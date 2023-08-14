from django.db import models
from manage import init_django  # only for standalone script

init_django()  # only for standalone script

from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)

class Genre(models.Model):
    genre_name = models.CharField(max_length=255, unique=True)

class Album(models.Model):
    album_name = models.CharField(max_length=255)
    album_year = models.DateField()

class Music(models.Model):
    music_name = models.CharField(max_length=255)
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)
    music_year = models.DateField()

class ListeningHistory(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    genre_points = models.IntegerField(default=0)  # Изменил на 0, так как вы упомянули "плюсуется балл"

class Recommendations(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    total_points = models.IntegerField()

    class Meta:
        unique_together = ('user', 'genre')
