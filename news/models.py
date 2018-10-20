from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    date = models.DateField(default=timezone.now, blank=False)
    headline = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)