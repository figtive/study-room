from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver


FACULTIES = [
    ('FK', 'FK'),
    ('FKG', 'FKG'),
    ('FKM', 'FKM'),
    ('FIK', 'FIK'),
    ('FF', 'FF'),
    ('FMIPA', 'FMIPA'),
    ('FT', 'FT'),
    ('FASILKOM', 'FASILKOM'),
    ('FH', 'FH'),
    ('FEB', 'FEB'),
    ('FIB', 'FIB'),
    ('FPsi', 'FPsi'),
    ('FISIP', 'FISIP'),
    ('FIA', 'FIA'),
    ('VOKASI', 'VOKASI'),
]

class UnionMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    # username = models.CharField(max_length=50, blank=False, null=False)
    # email = models.EmailField(max_length=50, blank=False, null=False)
    student_id = models.PositiveIntegerField(blank=False, null=False)
    faculty = models.CharField(max_length=10, choices=FACULTIES, blank=False, null=False)
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UnionMember.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# Create your models here.
