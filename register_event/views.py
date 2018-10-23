from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from event.models import Event
from .forms import RegisterEvent
from .models import RSVPMember

def register_event(request, event_id=None):
    print("ttt")
    print(event_id)
    if event_id is not None:
        response = {
            'form': RegisterEvent(),
            'event_id': event_id
        }
        return render(request, 'rsvp.html', response)
    else:
        return HttpResponseRedirect('/')

def register_event_auth(request, event_id=None):
    print("ttt AUTH")
    print(request.method)
    print(event_id)
    if event_id is not None:
        if (request.method == 'POST'):
            form = RegisterEvent(request.POST)
            if (form.is_valid()):
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                student_id = form.cleaned_data['student_id']
                faculty = form.cleaned_data['faculty']
                rsvp = RSVPMember(name=name, email=email, student_id=student_id, faculty=faculty)
                rsvp.save()
                event = Event.objects.get(id=event_id)
                event.participant_rsvp.add(rsvp)
                event.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/rsvp/register/')
    else:
        return HttpResponseRedirect('/')
