from django.shortcuts import render
from event.models import Event
from news.models import News

def index(request):
    response = {
        'all_event': Event.objects.all().order_by("date"),
        'all_news': News.objects.all().order_by("-date")
    }
    return render(request, 'index.html', response)
