from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


from event.models import Event
from .forms import LoginUser, RegisterUser, CompleteProfile
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
                user = authenticate(
                    request, username=username, password=password)
                if (user is not None):
                    login(request, user)
                    return HttpResponseRedirect('/user/profile/')
                else:
                    messages.error(
                        request, 'User not registered or pasword incorrect!')
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
                print("qwe")
                if password != ver_password:
                    messages.error(request, 'Passwords no not match!')
                    return HttpResponseRedirect('/user/register/')
                if not student_id_check(student_id):
                    messages.error(request, 'Student ID is invalid!')
                    return HttpResponseRedirect('/user/register/')
                if UnionMember.objects.filter(username=username).exists() or UnionMember.objects.filter(email=email).exists():
                    messages.error(
                        request, 'Username or email already registered!')
                    return HttpResponseRedirect('/user/register/')
                user = UnionMember.objects.create_user(name=name, username=username, email=email, password=password, student_id=student_id, faculty=faculty)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = 'Welcome to Study Room!'
                message = render_to_string('confirm_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token':account_activation_token.make_token(user),
                })
                sending_email = EmailMessage(
                            mail_subject, message, to=[email]
                )
                sending_email.send()





                # member = UnionMember(user=user, name=name, student_id=student_id, faculty=faculty)
                # member.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect('/user/profile/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/profile/')


def complete_profile(request):
    # print(request.user.student_id)
    if request.user.is_authenticated:
        if(request.user.student_id is not None and request.user.faculty is not None):
            return HttpResponseRedirect('../')
        if (request.method == 'POST'):
            form = CompleteProfile(request.POST)
            if (form.is_valid()):
                cleaned_data = form.cleaned_data
                student_id = cleaned_data['student_id']
                faculty = cleaned_data['faculty']
                if not student_id_check(student_id):
                    messages.error(request, 'Student ID is invalid!')
                    return HttpResponseRedirect('/user/register/')
                request.user.name = request.user.first_name + ' ' + request.user.last_name
                request.user.student_id = student_id
                request.user.faculty = faculty
                request.user.save()
                return HttpResponseRedirect('/user/profile/')
    response = {
        'form': CompleteProfile,
    }
    return render(request, 'complete-profile.html', response)
    

    # if (not request.user.is_authenticated):
    #     if (request.method == 'POST'):
    # form = RegisterUser(request.POST)
    # if (form.is_valid()):
    #     cleaned_data = form.cleaned_data
    #     name = cleaned_data['name']
    #     username = cleaned_data['username']
    #     email = cleaned_data['email']
    #     student_id = cleaned_data['student_id']
    #     faculty = cleaned_data['faculty']
    #     password = cleaned_data['password']
    #     ver_password = cleaned_data['ver_password']
    #     if password != ver_password:
    #         messages.error(request, 'Passwords no not match!')
    #         return HttpResponseRedirect('/user/register/')
    #     if not student_id_check(student_id):
    #         messages.error(request, 'Student ID is invalid!')
    #         return HttpResponseRedirect('/user/register/')
    #     if UnionMember.objects.filter(username=username).exists() or UnionMember.objects.filter(email=email).exists():
    #         messages.error(request, 'Username or email already registered!')
    #         return HttpResponseRedirect('/user/register/')
    #     user = UnionMember.objects.create_user(name=name, username=username, email=email, password=password, student_id=student_id, faculty=faculty)

    # member = UnionMember(user=user, name=name, student_id=student_id, faculty=faculty)
    # member.save()
    # login(request, user)
    #             return HttpResponseRedirect('/user/profile/')
    #     else:
    #         return HttpResponseRedirect('/')
    # else:
    #     return HttpResponseRedirect('/user/profile/')
def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UnionMember.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for confirming yout email!')
        return HttpResponseRedirect('/user/profile/')
    else:
        messages.error(request, 'Activation link invalid!')
        return HttpResponseRedirect('/user/register/')
        # make page just for this, have a resend activation link
