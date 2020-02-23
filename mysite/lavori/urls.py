from django.urls import path
from .views import lavori

urlpatterns = [
    path("lavori/", lavori, name='lavori')
]
