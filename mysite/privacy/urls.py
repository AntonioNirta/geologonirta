from django.urls import path
from .views import privacy

urlpatterns = [
    path("privacy/", privacy, name='privacy')
]
