from django.db import models
from django.db.models.signals import post_save

# Create your models here.
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

class RSVPMember(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    student_id = models.PositiveIntegerField(blank=False, null=False)
    faculty = models.CharField(max_length=10, choices=FACULTIES, blank=False, null=False)


    def __str__(self):
        return "RSVP: " + self.name