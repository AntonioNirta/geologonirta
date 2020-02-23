from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this


# Create your views here.

def cookies(request):
    return render(request, "cookie-policy.html")
