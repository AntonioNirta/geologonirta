from django.shortcuts import render
from django.http import HttpResponse
#from .models import Lavoro

# Create your views here.

def contatti(request):
    return render(request, "contatti.html")
