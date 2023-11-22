#views.py file
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})#{} passes in python dictionary

def about(request):
    return render(request, 'about.html', {})#{} passes in python dictionary
