from django.test import TestCase, Client
from django.apps import apps
from django.contrib.auth import get_user

# Create your tests here.
from django.db import models
from django.utils import timezone

from django.urls import resolve
from .views import event
from .models import Event
from .apps import EventConfig

test_user_data = {
    'name': 'John Appleseed',
    'email': 'john@email.com',
    'username': 'john.apple',
    'student_id': '1706019791',
    'faculty': 'FASILKOM',
    'password': 'password',
    'ver_password': 'password'
}

test_user_login = {
    'username': test_user_data['username'],
    'password': test_user_data['password'],
}

test_event = {
    'name': 'Compfest X',
    'date': timezone.now(),
    'location': 'Balairung',
    'description': 'acara Compfest tahun ini',
    'participant_user': [test_user_data],
}

class Event_Test(TestCase):
    def test_event_is_exist(self):
        response = self.client.get('/event/')
        self.assertEqual(response.status_code,200)
    
    def test_url_not_exist(self):
        response = Client().get('/doesnotexist/')
        self.assertTemplateUsed(response, '404.html')

    def test_app_config(self):  
        self.assertEqual(EventConfig.name, 'event')
        self.assertEqual(apps.get_app_config('register_user').name, 'register_user')
        
    def test_check_model_name(self):
        event = Event(name="Name", date=timezone.now(),  location="loc", description="desc")
        event_name = str(event)
        self.assertEqual(event_name,"Name")
    
    def test_template_login(self):
        response = self.client.get('/event/')
        self.assertTemplateUsed(response, 'event.html')

    def test_event_attend(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.post('/user/login/auth/', test_user_login)
        event = Event(name="Name", date=timezone.now(),  location="loc", description="desc")
        event.save()
        response = self.client.get('/event/attend/' + str(event.id))
        # print(get_user(self.client))
        # print(event.participant_user.all())
        self.assertTrue(get_user(self.client) in event.participant_user.all())

    def test_event_leave(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.post('/user/login/auth/', test_user_login)
        event = Event(name="Name", date=timezone.now(),  location="loc", description="desc")
        event.save()
        response = self.client.get('/event/attend/' + str(event.id))
        # print(get_user(self.client))
        # print(event.participant_user.all())
        response = self.client.get('/event/leave/' + str(event.id))
        self.assertTrue(get_user(self.client) not in event.participant_user.all())