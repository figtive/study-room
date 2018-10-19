from django.test import TestCase,Client

# Create your tests here.
from django.db import models
from django.utils import timezone

from django.urls import resolve
from .views import event
from .models import Event

class Event_Test(TestCase):
    def test_event_is_exist(self):
        response = Client().get('/event/')
        self.assertEqual(response.status_code,200)
    
    def test_url_not_exist(self):
        response = Client().get('doesnotexist')
        self.assertEqual(response.status_code,404)

    def test_check_model_name(self):
        event = Event(name="Name", date=timezone.now(),  location="loc", description="desc")
        event_name = str(event)
        self.assertEqual(event_name,"Name")