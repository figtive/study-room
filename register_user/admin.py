from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UnionMember

class CustomUserAdmin(UserAdmin):
    model = UnionMember
    list_display = ['email', 'username', 'faculty', 'student_id']
 
admin.site.register(UnionMember)
