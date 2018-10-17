from django.shortcuts import render
from event.models import Event

def index(request):
    response = {
        'all_event': Event.objects.all().order_by("date")
    }
    return render(request, 'index.html', response)
