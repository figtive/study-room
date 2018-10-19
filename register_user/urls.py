from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/auth/', views.login_auth, name="login_auth"),
    path('register/', views.register_user, name="register"),
    path('register/auth/', views.register_auth, name="register_auth"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
]
