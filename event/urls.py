from django.urls import path

from . import views

urlpatterns = [
    path('', views.event, name ="event"),
    path('attend/<int:id>', views.event_attend, name="event_attend"),
    path('leave/<int:id>', views.event_leave, name="event_leave"),
]
