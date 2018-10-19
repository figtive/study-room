from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Event

def event(request):
    all_events = Event.objects.all()
    response = {
        'all_event' : all_events,
    }
    print(Event.objects.all())
    return render(request,'event.html',response)