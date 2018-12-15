from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import About
from .forms import aboutForm

def about(request):
    add_about = aboutForm()
    all_about = About.objects.all()[::-1]
    response = {
        'form': add_about,
        'all_about': all_about,
    }
    return render(request, 'about.html', response)  

def add_about(request):
    if request.method == "POST":
        form = aboutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            about = About(author=request.user.name, content=cleaned_data['about_post'])
            about.save()  
            return JsonResponse(data={"success": "true"}, status=202)
    return JsonResponse(data={"success": "false"}, status=406)