from django.urls import path
from .views import servizi

urlpatterns = [
    path("servizi/", servizi, name='servizi')
]
