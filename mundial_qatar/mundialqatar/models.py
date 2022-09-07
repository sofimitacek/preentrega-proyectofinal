from django.db import models

class Seleccion(models.Model):
    pais = models.CharField(max_length=128)


class Estadio(models.Model):
    ciudad = models.CharField(max_length=128)

class Arbitro(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=128)