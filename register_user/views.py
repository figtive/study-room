from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from .forms import LoginUser, RegisterUser
from .models import UnionMember
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/user/login/')
def profile(request):
    response = {
    }
    return render(request, 'profile.html', response)

def login_user(request):
    if (not request.user.is_authenticated):
        response = {
            'form': LoginUser,
        }
        return render(request, 'login.html', response)
    else:
        return HttpResponseRedirect('/user/profile/')




def logout_user(request):
    if (request.user.is_authenticated):
        logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    if (not request.user.is_authenticated):
        response = {
            'form': RegisterUser,
        }
        return render(request, 'register.html', response)
    else:
        return HttpResponseRedirect('/user/profile/')

def login_auth(request):
    if (not request.user.is_authenticated):
        if (request.method == 'POST'):
            form = LoginUser(request.POST)
            if (form.is_valid()):
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if (user is not None):
                    login(request, user)
                    return HttpResponseRedirect('/user/profile/')
                else:
                    raise forms.ValidationError('user not registered or password incorrect')
        else:
            return HttpResponseRedirect('/')
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
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    user = User.objects.create_user(email=email, username=username, password=password)
                    member = UnionMember(user=user, name=name, student_id=student_id, faculty=faculty)
                    member.save()
                    return HttpResponseRedirect('/user/login/')
                else:
                    raise forms.ValidationError('username or email already registered')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/profile/')
        
