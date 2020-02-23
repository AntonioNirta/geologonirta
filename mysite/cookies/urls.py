from django.urls import path
from .views import cookies

urlpatterns = [
    path("cookies/", cookies, name='cookies')
]
