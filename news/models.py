from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    content = models.TextField()