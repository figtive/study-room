from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .forms import RegisterEvent
from .models import UnionEvent



# Create your views here.

def register_event(request):
    posted = UnionEvent.objects.all()
    if (request.method == 'POST'):
        form = RegisterEvent(request.POST)
            if (form.is_valid()):

                form.save()

                return HttpResponseRedirect('/event/register/')

    else :

        form = RegisterEvent()
        context = {
        'Posts' : posted,
        'RegisterEvent' : form,
        }      

    return HttpResponseRedirect('/event/register/')        
        
