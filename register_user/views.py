from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_token


from event.models import Event
from .forms import LoginUser, RegisterUser, CompleteProfile, ForgetPassword, ResetPassword
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
    reverse = request.GET.get('reverse', None)
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
                if (user is not None and user.is_active):
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return HttpResponseRedirect('/user/profile/')
                elif (user is not None and not user.is_active):
                    messages.error(request, 'Check your email to activate your account!')
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
                    messages.error(
                        request, 'Username or email already registered!')
                    return HttpResponseRedirect('/user/register/')
                user = UnionMember.objects.create_user(name=name, username=username, email=email, password=password, student_id=student_id, faculty=faculty)
                user.is_active = False
                user.save()
                send_email(request, user, 'Welcome to Study Room!', 'confirm-email.html')
                messages.success(request, 'Welcome! Check your email to activate your account!')
                return HttpResponseRedirect('/user/login/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/profile/')


def complete_profile(request):
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
    

def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UnionMember.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UnionMember.DoesNotExist):
        user = None
    if user is not None and account_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for confirming your email!')
        return HttpResponseRedirect('/user/profile/')
    else:
        messages.error(request, 'Activation link invalid!')
        return HttpResponseRedirect('/user/register/')
        # make page just for this, have a resend activation link

def forget_password(request):
    if (not request.user.is_authenticated):
        response = {
            'form': ForgetPassword,
        }
        return render(request, 'forget.html', response)
    else:
        return HttpResponseRedirect('/user/profile/')

def forget_password_auth(request):
    if (not request.user.is_authenticated):
        if (request.method == 'POST'):
            form = ForgetPassword(request.POST)
            if (form.is_valid()):
                cleaned_data = form.cleaned_data
                email = cleaned_data['email']
                try:
                    user = UnionMember.objects.get(email=email)
                except(UnionMember.DoesNotExist):
                    user = None
                if user is not None:
                    print(user)
                    send_email(request, user, "Password Reset", "reset-email.html")
                    messages.success(request, 'Password reset link has been sent to your email!')
    return HttpResponseRedirect('/user/forget/')


def reset_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UnionMember.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UnionMember.DoesNotExist):
        user = None
    if user is not None and account_token.check_token(user, token):
        response = {
            'success': False,
            'form': ResetPassword,
            'uid': uidb64,
            'token': token
        }
        return render(request, 'reset.html', response)
    else:
        messages.error(request, 'Password reset link invalid!')
        return HttpResponseRedirect('/user/register/')



def reset_password_auth(request, uidb64, token):
    if (not request.user.is_authenticated):
        if (request.method == 'POST'):
            form = ResetPassword(request.POST)
            if (form.is_valid()):
                cleaned_data = form.cleaned_data
                password = cleaned_data['password']
                ver_password = cleaned_data['ver_password']
                try:
                    uid = force_text(urlsafe_base64_decode(uidb64))
                    user = UnionMember.objects.get(pk=uid)
                except(TypeError, ValueError, OverflowError, UnionMember.DoesNotExist):
                    user = None
                if user is not None and account_token.check_token(user, token):
                    if password != ver_password:
                        messages.error(request, 'Passwords no not match!')
                        return HttpResponseRedirect('/user/register/')
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'You have successfully changed your password!')
                    return HttpResponseRedirect('/user/login/')
                else:
                    messages.error(request, 'Password reset link invalid!')
                    return HttpResponseRedirect('/user/register/')
    else:
        return HttpResponseRedirect('/user/register/')





def send_email(request, user, email_subject, template):
    print(user)
    current_site = get_current_site(request)
    message = render_to_string(template, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_token.make_token(user),
    })
    sending_email = EmailMultiAlternatives(email_subject, strip_tags(message), "studyroom.fstudios@gmail.com", [user.email])
    sending_email.attach_alternative(message, "text/html")
    sending_email.send()

