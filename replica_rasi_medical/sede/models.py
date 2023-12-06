from django.db import models
from dj_cqrs.mixins import ReplicaMixin
from django.utils import timezone

class Sede(ReplicaMixin, models.Model):

    CQRS_ID = 'sede_model'
    CQRS_CUSTOM_SERIALIZATION = True

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    
    cqrs_revision = models.IntegerField(default=0)
    cqrs_update = models.DateTimeField(default=timezone.now)

    def __str__(self):  
        return self.nombre

    
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        return Sede.objects.create(
            id=mapped_data['id'],
            nombre=mapped_data['nombre'],
            direccion=mapped_data['direccion'],
            telefono=mapped_data['telefono'],
            ciudad=mapped_data['ciudad'],
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )


    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
        self.id=mapped_data['id']
        self.nombre=mapped_data['nombre']
        self.direccion=mapped_data['direccion']
        self.telefono=mapped_data['telefono']
        self.ciudad=mapped_data['ciudad']
        self.cqrs_revision=mapped_data['cqrs_revision']
        self.cqrs_updated=mapped_data['cqrs_updated']
        self.save()
        return self