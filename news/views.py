from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import News


def news(request):
    all_news = News.objects.all().order_by("-news_date")
    response = {
        'all_news': all_news,
    }
    return render(request, 'news.html', response)
