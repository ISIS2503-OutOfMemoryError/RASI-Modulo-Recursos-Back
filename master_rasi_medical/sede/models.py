from django.db import models
from dj_cqrs.mixins import MasterMixin

class Sede(MasterMixin, models.Model):

    CQRS_ID = 'sede_model'

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)

    def __str__(self):  
        return self.nombre
