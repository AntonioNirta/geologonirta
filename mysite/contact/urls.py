# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import contatti

urlpatterns = [
    path('contatti/', contatti, name='contact'),
    #path('success/', successView, name='success'),
]
