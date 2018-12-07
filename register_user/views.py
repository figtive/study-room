from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from event.models import Event
from .forms import LoginUser, RegisterUser
from .models import UnionMember

def student_id_check(id):
    if (len(id) == 10):
        even = 0
        odd = 0
        for i in range(9):
            if i % 2 == 0:
                even += 3 * int(id[i])
            else:
                odd += int(id[i])
        return (even + odd) % 7 == int(id[9])
    else:
        return False

def username_check(request):
    username = request.GET.get('username', None)
    if not UnionMember.objects.filter(username__iexact=username).exists():
        return JsonResponse(data={'status': 'true'}, status=202)
    return JsonResponse(data={'status': 'false'}, status=406)

def email_check(request):
    email = request.GET.get('email', None)
    if not UnionMember.objects.filter(email__iexact=email).exists():
        return JsonResponse(data={'status': 'true'}, status=202)
    return JsonResponse(data={'status': 'false'}, status=406)

@login_required(login_url='/user/login/')
def profile(request):
    response = {
        'all_event': Event.objects.all().filter(participant_user=request.user)
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
                    messages.error(request, 'User not registered or pasword incorrect!')
                    return HttpResponseRedirect('/user/login/')
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
                ver_password = cleaned_data['ver_password']
                if password != ver_password:
                    messages.error(request, 'Passwords no not match!')
                    return HttpResponseRedirect('/user/register/')
                if not student_id_check(student_id):
                    messages.error(request, 'Student ID is invalid!')
                    return HttpResponseRedirect('/user/register/')
                if UnionMember.objects.filter(username=username).exists() or UnionMember.objects.filter(email=email).exists():
                    messages.error(request, 'Username or email already registered!')
                    return HttpResponseRedirect('/user/register/')
                user = UnionMember.objects.create_user(name=name, username=username, email=email, password=password, student_id=student_id, faculty=faculty)
                # member = UnionMember(user=user, name=name, student_id=student_id, faculty=faculty)
                # member.save()
                login(request, user)
                return HttpResponseRedirect('/user/profile/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/profile/')
