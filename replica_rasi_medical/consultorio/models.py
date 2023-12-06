from django.db import models
from sede.models import Sede
from equipo_medico.models import EquipoMedico
from dj_cqrs.mixins import ReplicaMixin

class Consultorio(ReplicaMixin, models.Model):

    CQRS_ID = 'consultorio_model'
    CQRS_CUSTOM_SERIALIZATION = True

    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    #Esta realción es uno a uno, toca cabiarla uno a muchos
    #Es decir, un consultorio puede tener varios equipos médicos
    equipo_medico = models.ForeignKey(EquipoMedico, on_delete=models.CASCADE)   
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
