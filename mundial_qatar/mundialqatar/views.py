from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from mundialqatar.models import Seleccion, Estadio, Arbitro

def probandoTemplate(request):
    html_1 = open("C:/Users/chofy/OneDrive/Documentos/proyectosAA/mundial/mundial_qatar/templates/plantilla.html")
    lista_selecciones = Seleccion.objects.all()
    diccionario = {'selecciones': lista_selecciones}
    plantilla = Template(html_1.read())
    html_1.close()
    contexto_1 = Context(diccionario)
    documento = plantilla.render(contexto_1)

    return HttpResponse(documento)
