from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


from Selecciones.models import Players, Coachs_Staff
from Selecciones.forms import Player_form, Coachs_Staff_form

class PlayersListView( ListView):
    model = Players    template_name = 'Selecciones/Players.html'


class PlayersreateView( CreateView):
    model = Players    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('Players')


class PlayerspdateView( UpdateView):
    model = Players    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('Players')


class PlayerseleteView( DeleteView):
    model = Players    success_url = reverse_lazy('Players')

# Create your views here.
