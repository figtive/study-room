from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Event

def event(request):
    all_events = Event.objects.all()
    response = {
        'all_events' : all_events,
    }
    return render(request,'event.html',response)