from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=100, blank=False, null=True)
    student_id = models.PositiveIntegerField(blank=False, null=True)
    faculty = models.CharField(max_length=100, blank=False, null=True)
    

# Create your models here.
