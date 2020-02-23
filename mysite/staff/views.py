from django.shortcuts import render
from django.http import HttpResponse
from .models import Membro

# Create your views here.

def chisono(request):
    membro = Membro.objects.all()
    context = {"membro": membro}
    print(context)
    return render(request, "chi-sono.html", context)
