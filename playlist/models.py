from django.db import models


# Create your models here.
class VibeCheck(models.Model):
    artist1 = models.CharField(max_length=50, blank=False)
    artist2 = models.CharField(max_length=50, blank=False)
    artist3 = models.CharField(max_length=50, blank=False)
    artist4 = models.CharField(max_length=50, blank=False)
    artist5 = models.CharField(max_length=50, blank=False)


class GenrePick(models.Model):
    genres = [
        ('', '--What You In The Mood For--'),
        ('Indie', 'Indie'),
        ('Pop', 'Pop'),
        ('Country', 'Country'),
        ('Hip-Hop', 'Hip-Hop'),
        ('Workout', 'Workout'),
        ('R&B', 'R&B'),
        ('Dance/Electronic', 'Dance/Electronic'),
        ('Chill', 'Chill'),
        ('Christian & Gospel', 'Christian & Gospel'),
        ('Sleep', 'Sleep')
    ]
