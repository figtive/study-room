from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('add-about/', views.add_about, name='add-about'),
]
