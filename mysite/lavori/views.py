from django.shortcuts import render
from django.http import HttpResponse
from .models import Lavoro

# Create your views here.

def lavori(request):
    lavori = Lavoro.objects.all().order_by('anno')
    context = {"lavori": lavori}
    print(context)
    return render(request, "lavori.html", context)
