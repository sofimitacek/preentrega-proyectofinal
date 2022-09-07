from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from mundialqatar.models import Seleccion, Estadio, Arbitro

def probandotemplate(self):
    html1 = open("C:\\Users\\chofy\\OneDrive\\Documentos\\proyectosAA\\mundial\\mundial_qatar\\templates.html")
    plantilla = Template(html1.read())
    html1.close()
    contexto1 = Context()
    documento = plantilla.render(contexto1)

    return HttpResponse(documento)
