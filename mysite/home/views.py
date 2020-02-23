from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this


# Create your views here.

def home(request):
    return render(request, "home.html")
