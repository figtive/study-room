from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30, blank=False, null=True)
    date = models.DateField(default=timezone.now())
    location = models.CharField(max_length=50, blank=False, null=True)
    # description is used for aesthetics. Discard if this destroys flexibility 
    description = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name
