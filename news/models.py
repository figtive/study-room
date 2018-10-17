from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_author = models.CharField(max_length=50)
    news_date = models.DateField(default=timezone.now)
    news_content = models.TextField()