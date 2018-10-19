from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Event


def event(request):
    user_attends = {}
    for event in Event.objects.all():
        user_attends['event.id'] = Event.objects.all().filter(participant_user=request.user).exists()
    response = {
        'all_event': Event.objects.all().order_by("date"),
        'user_attends': user_attends,
    }
    return render(request, 'event.html', response)

def event_attend(request,id = None):
    if id:
        event = Event.objects.get(id = id)
        user = request.user
        event.participant_user.add(user)
        event.save()
        
    return HttpResponseRedirect('/event/')