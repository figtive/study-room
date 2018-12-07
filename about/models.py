from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class About(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date = models.DateField(default=timezone.now, blank=False)
