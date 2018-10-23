from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/<int:event_id>', views.register_event, name="register_event"),
    path('register/auth/<int:event_id>', views.register_event_auth, name="register_event_auth"),
]
