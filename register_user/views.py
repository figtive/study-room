from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout


from .forms import RegisterUser
from .models import UnionMember
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/user/login/')
def profile(request):
    response = {
    }
    return render(request, 'profile.html', response)


def logout_user(request):
    if (request.user.is_authenticated):
        logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if (not request.user.is_authenticated):
        response = {
            'form': RegisterUser,
        }
        return render(request, 'register.html', response)
    else:
        return HttpResponseRedirect('/user/profile/')


def register_auth(request):
    if (not request.user.is_authenticated):
        if (request.method == 'POST'):
            form = RegisterUser(request.POST)
            if (form.is_valid()):
                cleaned_data = form.cleaned_data
                name = cleaned_data['name']
                username = cleaned_data['username']
                email = cleaned_data['email']
                student_id = cleaned_data['student_id']
                faculty = cleaned_data['faculty']
                password = cleaned_data['password']
                if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    user = User.objects.create_user(email=email, username=username, password=password)
                    member = UnionMember(user=user, name=name, student_id=student_id, faculty=faculty)
                    # user.save()
                    member.save()
                else:
                    raise forms.ValidationError('already registered')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/profile/')
        
