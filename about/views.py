from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# from .models import

response = {}


def about(request):
    # all_news = News.objects.all().order_by("-date")
    # response = {
    #     'all_news': all_news,
    # }
    return render(request, 'about.html', response)
