from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/auth/', views.login_auth, name="login_auth"),
    path('register/', views.register_user, name="register"),
    path('register/auth/', views.register_auth, name="register_auth"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('register/username_check/', views.username_check, name="username_check"),
    path('register/email_check/', views.email_check, name="email_check"),
    path('complete_profile', views.complete_profile, name="complete_profile"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_user, name="activate_user"),
]
