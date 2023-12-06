from django.db import models
from sede.models import Sede
from equipo_medico.models import EquipoMedico
from dj_cqrs.mixins import ReplicaMixin
from django.utils import timezone

class Consultorio(ReplicaMixin, models.Model):

    CQRS_ID = 'consultorio_model'
    CQRS_CUSTOM_SERIALIZATION = True

    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    #Esta realción es uno a uno, toca cabiarla uno a muchos
    #Es decir, un consultorio puede tener varios equipos médicos
    equipo_medico = models.ForeignKey(EquipoMedico, on_delete=models.CASCADE)  
    
    cqrs_revision = models.IntegerField(default=0)
    cqrs_update = models.DateTimeField(default=timezone.now)


    def __str__(self):  
        return self.nombre
    

    @staticmethod
    def _handle_sede(mapped_data):
        sede = Sede.objects.get(pk=mapped_data)
        return sede


    @staticmethod 
    def _handle_equipo_medico(mapped_data):
        equipo_medico = EquipoMedico.objects.get(pk=mapped_data)
        return equipo_medico
    

    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        print(mapped_data['sede'])
        sede = cls._handle_sede(mapped_data['sede'])
        print(mapped_data['equipo_medico'])
        equipo_medico = cls._handle_equipo_medico(mapped_data['equipo_medico'])

        return Consultorio.objects.create(
            id=mapped_data['id'],
            numero=mapped_data['numero'],
            sede=sede,
            equipo_medico=equipo_medico,
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )
    

    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
        print(mapped_data['sede'])
        sede = self._handle_sede(mapped_data['sede'])
        print(mapped_data['equipo_medico'])
        equipo_medico = self._handle_equipo_medico(mapped_data['equipo_medico'])
        self.id=mapped_data['id']
        self.numero=mapped_data['numero']
        self.sede=sede
        self.equipo_medico=equipo_medico
        self.cqrs_revision=mapped_data['cqrs_revision']
        self.cqrs_updated=mapped_data['cqrs_updated']
        self.save()
        return self
