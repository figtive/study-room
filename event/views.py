from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Event


def event(request):
    response = {
        'all_event': Event.objects.all().order_by("date"),
    }
    return render(request, 'event.html', response)

def event_attend(request,id = None):
    if request.user.is_authenticated:
        if id:
            event = Event.objects.get(id=id)
            user = request.user
            event.participant_user.add(user)
            event.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def event_leave(request,id = None):
    if request.user.is_authenticated:
        if id:
            event = Event.objects.get(id=id)
            user = request.user
            event.participant_user.remove(user)
            event.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
