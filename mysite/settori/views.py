from django.shortcuts import render
from django.http import HttpResponse
from .models import Settore

# Create your views here.

#def homepage(request):
    #return HttpResponse('<h1>HomePage</h1>')

#def homepage(request):

    #s = []

    #for sett in Settore.objects.all():
        #s.append(sett.titolo)

    #response = str(s)
    #print(response)


    #return HttpResponse("<h1>" + response + "</h1>")


def servizi(request):
    servizi = Settore.objects.all()
    context = {"servizi": servizi}
    print(context)
    return render(request, "servizi.html", context)
