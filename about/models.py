from django.db import models
from django.utils import timezone
from register_user.models import UnionMember

# Create your models here.

class About(models.Model):
    author = models.CharField(max_length=50, blank=False, null=True)
    content = models.TextField(blank=False)
    date = models.DateField(default=timezone.now, blank=False)
