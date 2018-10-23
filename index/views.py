from event.models import Event
from news.models import News
from django.shortcuts import render


def index(request):
    response = {
        'all_event': Event.objects.all().order_by("date")[:5],
        'all_news': News.objects.all().order_by("date")[:6]
    }
    return render(request, 'index.html', response)


def error_404(request):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '404.html', data)