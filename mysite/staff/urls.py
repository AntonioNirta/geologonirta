from django.urls import path
from .views import chisono

urlpatterns = [
    path("staff/", chisono, name='chisono')
]
