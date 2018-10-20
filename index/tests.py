from django.apps import apps
from django.test import TestCase
from django.urls import resolve
from django.utils import timezone

from event.models import Event
from news.models import News
from .apps import IndexConfig
from . import views

class IndexTest(TestCase):

    def test_index_exist(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
        
    def test_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_func_index(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_app_config(self):
        self.assertEqual(IndexConfig.name, 'index')
        self.assertEqual(apps.get_app_config('index').name, 'index')

    def test_max_event(self):
        for i in range(10):
            event = Event(name="Event" + str(i), date=timezone.now(), location="Location", description="Description")
            event.save()
        response = self.client.get('/')
        self.assertLessEqual(response.context['all_event'].count(), 5)
        
    def test_max_news(self):
        for i in range(10):
            news = News(title="News" + str(i), author="Author", headline="Description", content="Content")
            news.save()
        response = self.client.get('/')
        self.assertLessEqual(response.context['all_news'].count(), 6)
