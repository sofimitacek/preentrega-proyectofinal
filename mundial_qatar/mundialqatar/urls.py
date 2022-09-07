from django.urls import path
from mundialqatar.views import probandoTemplate


urlpatterns = [
    path('', probandoTemplate),
]