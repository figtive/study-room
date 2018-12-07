from django.db import models
from django.utils import timezone
from register_user.models import UnionMember

# Create your models here.

class About(models.Model):
    user = models.OneToOneField(UnionMember, blank=True, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date = models.DateField(default=timezone.now, blank=False)
