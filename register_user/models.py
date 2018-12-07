from django.db import models
from django.contrib.auth.models import AbstractUser

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

# class UnionMemberManager(UserManager):
#     pass

class UnionMember(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    # username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    # password = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    student_id = models.PositiveIntegerField(blank=False, null=False)
    faculty = models.CharField(max_length=10, choices=FACULTIES, blank=False, null=False)
    REQUIRED_FIELDS = ['name', 'email', 'student_id', 'faculty']
