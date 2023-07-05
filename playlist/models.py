from django.db import models


# Create your models here.
class VibeCheck(models.Model):
    artist1 = models.CharField(max_length=50, blank=False)
    artist2 = models.CharField(max_length=50, blank=False)
    artist3 = models.CharField(max_length=50, blank=False)
    artist4 = models.CharField(max_length=50, blank=False)
    artist5 = models.CharField(max_length=50, blank=False)
