from django.test import TestCase, Client
from django.urls import resolve
from django.apps import apps

from .views import about
from .apps import AboutConfig

class TestNews(TestCase):
    def test_using_status_function(self):
        response = resolve('/about/')
        self.assertEqual(response.func, about)

    def test_url_exists(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_doesnt_exists(self):
        response = Client().get('/nothing/')
        self.assertTemplateUsed(response, '404.html')

    def test_app_config(self):
        self.assertEqual(AboutConfig.name, 'about')
        self.assertEqual(apps.get_app_config('about').name, 'about')
