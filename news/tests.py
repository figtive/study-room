from django.test import TestCase, Client
from django.urls import resolve
from django.apps import apps

from .views import news
from .apps import NewsConfig

# Create your tests here.

class TestNews(TestCase):
    def test_using_status_function(self):
        response = resolve('/news/')
        self.assertEqual(response.func, news)

    def test_url_exists(self):
        response = Client().get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_url_doesnt_exists(self):
        response = Client().get('/nothing/')
        self.assertEqual(response.status_code, 404)

    def test_app_config(self):
        self.assertEqual(NewsConfig.name, 'news')
        self.assertEqual(apps.get_app_config('news').name, 'news')