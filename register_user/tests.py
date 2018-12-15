from django.apps import apps
from django.forms import ValidationError
from django.test import TestCase, Client
from django.urls import resolve
from django.contrib.auth import get_user
from django.contrib.messages import get_messages

# from .apps import RegisterUserConfig
from .forms import LoginUser, RegisterUser
from .models import UnionMember
from .views import student_id_check
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

test_user_data_fail1 = {
    'name': 'John Appleseed',
    'email': 'john@email.com',
    'username': 'john.apple',
    'student_id': '1706019791',
    'faculty': 'FASILKOM',
    'password': 'password',
    'ver_password': 'passkey123'
}

test_user_data_fail2 = {
    'name': 'John Appleseed',
    'email': 'john@email.com',
    'username': 'john.apple',
    'student_id': '170',
    'faculty': 'FASILKOM',
    'password': 'password',
    'ver_password': 'password'
}

test_user_login = {
    'username': test_user_data['username'],
    'password': test_user_data['password'],
}

test_user_login_fail = {
    'username': test_user_data['username'],
    'password': 'passkey123',
}

class TestRegisterUser(TestCase):

    def test_user_register(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user_count = UnionMember.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_login(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_user_logout(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/logout/')
        response = self.client.get('/')
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_user_profile(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/profile/')
        self.assertContains(response, test_user_data['name'])

    def test_user_display_index(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
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
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
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
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
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
        user = UnionMember.objects.create_user(email=test_user_data['email'], username=test_user_data['username'], password=test_user_data['password'])
        user_count = UnionMember.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_form_validate_register(self):  
        form = RegisterUser(data=test_user_data)
        self.assertTrue(form.is_valid())
        
    def test_form_validate_login(self):  
        form = LoginUser(data=test_user_login)
        self.assertTrue(form.is_valid())

    def test_redirect_register_auth(self):
        response = self.client.get('/user/register/auth/')
        self.assertRedirects(response, '/')
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/register/auth/')
        self.assertRedirects(response, '/user/profile/')

    def test_redirect_login_auth(self):
        response = self.client.get('/user/login/auth/')
        self.assertRedirects(response, '/')
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/login/auth/')
        self.assertRedirects(response, '/user/profile/')
        
    def test_redirect_register(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/register/')
        self.assertRedirects(response, '/user/profile/')

    def test_redirect_login(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        user = UnionMember.objects.get(email=test_user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post('/user/login/auth/', test_user_login)
        response = self.client.get('/user/login/')
        self.assertRedirects(response, '/user/profile/')

    def test_error_register(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        self.assertRedirects(response, '/user/login/')
        response = self.client.post('/user/register/auth/', test_user_data)
        self.assertRedirects(response, '/user/register/')
        
    def test_error_login(self):
        response = self.client.post('/user/login/auth/', test_user_login_fail)
        self.assertRedirects(response, '/user/login/')

    def test_form_validation1(self):
        response = self.client.post('/user/register/auth/', follow=True, data=test_user_data_fail1)
        self.assertRedirects(response, '/user/register/')
    
    def test_form_validation2(self):
        response = self.client.post('/user/register/auth/', follow=True, data=test_user_data_fail2)
        self.assertRedirects(response, '/user/register/')

    # def test_app_config(self):
    #     self.assertEqual(RegisterUserConfig.name, 'register_user')
    #     self.assertEqual(apps.get_app_config('register_user').name, 'register_user')

    def test_student_id_check(self):
        self.assertTrue(student_id_check('1706019791'))
        self.assertTrue(student_id_check('1706067512'))
        self.assertFalse(student_id_check('1231231231'))
        self.assertFalse(student_id_check('1'))
        self.assertFalse(student_id_check(''))

    def test_email_exist(self):
        response = self.client.post('/user/register/auth/', follow=True, data=test_user_data)
        response = self.client.get('/user/register/email_check/', data={
            'email': 'mail@email.com',
        })
        self.assertTrue(response.status_code, 202)
        response = self.client.get('/user/register/email_check/', data={
            'email': 'john@email.com',
        })
        self.assertTrue(response.status_code, 406)

    def test_username_exist(self):
        response = self.client.post('/user/register/auth/', follow=True, data=test_user_data)
        response = self.client.get('/user/register/username_check/', data={
            'username': 'john',
        })
        self.assertTrue(response.status_code, 202)
        response = self.client.get('/user/register/username_check/', data={
            'username': 'john.apple',
        })
        self.assertTrue(response.status_code, 406)

    def test_prompt_activation(self):
        response = self.client.post('/user/register/auth/', test_user_data)
        response = self.client.post('/user/login/auth/', follow=True, data=test_user_login)
        self.assertContains(response, 'Check your email to activate your account!')
        
