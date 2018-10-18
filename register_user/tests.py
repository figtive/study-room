from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib.auth import get_user

from .forms import LoginUser, RegisterUser
from . import views

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

class TestRegisterUser(TestCase):

    def test_user_register(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_login(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_user_logout(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        response = self.client.get('/user/logout/')
        response = self.client.get('/')
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_user_profile(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        response = self.client.get('/user/profile/')
        self.assertContains(response, test_user_data['name'])

    def test_user_display_index(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        response = self.client.get('/')
        self.assertContains(response, test_user_data['username'].upper())

    def test_register_exists(self):
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code,200)

    def test_login_exists(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code,200)

    def test_profile_exists(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code,200)

    def test_template_login(self):
        response = self.client.get('/user/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_template_register(self):
        response = self.client.get('/user/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_template_profile(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.login(username=test_user_login['username'], password=test_user_login['password'])
        response = self.client.get('/user/profile/')
        self.assertTemplateUsed(response, 'profile.html')

    def test_func_register(self):
        found = resolve('/user/register/')
        self.assertEqual(found.func, views.register_user)
        
    def test_func_login(self):
        found = resolve('/user/login/')
        self.assertEqual(found.func, views.login_user)
        
    def test_func_profile(self):
        found = resolve('/user/profile/')
        self.assertEqual(found.func, views.profile)        

    def test_model_user(self):
        user = User.objects.create_user(email=test_user_data['email'], username=test_user_data['username'], password=test_user_data['password'])
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_form_validate_register(self):  
        form = RegisterUser(data=test_user_data)
        self.assertTrue(form.is_valid())
        
    def test_form_validate_login(self):  
        form = LoginUser(data=test_user_login)
        self.assertTrue(form.is_valid())
