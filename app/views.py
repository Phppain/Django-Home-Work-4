from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(render(request, 'home.html'))

def about(request):
    return HttpResponse(render(request, 'about.html'))

def contacts(request):
    return HttpResponse(render(request, 'contacts.html'))
