from django.db import models
from sede.models import Sede
from dj_cqrs.mixins import ReplicaMixin
from django.utils import timezone

class EquipoMedico(ReplicaMixin, models.Model):

    CQRS_ID = 'equipo_medico_model'
    CQRS_CUSTOM_SERIALIZATION = True

    # Definir las opciones para el tipo de equipo como una tupla de tuplas
    TIPO_EQUIPO_CHOICES = (
        ('Standard', 'Standard'),
        ('ECG', 'ECG'),
        ('Desfibrilador', 'Desfibrilador'),
        ('Luz', 'Luz'),
        ('Esterilizador', 'Esterilizador'),
        ('Ventilador', 'Ventilador'),
    )

    #Atributos
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    tipo_equipo = models.CharField(max_length=20, choices=TIPO_EQUIPO_CHOICES, default='Standard')
    #Relaciones
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
    
    cqrs_revision = models.IntegerField(default=0)
    cqrs_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo_equipo
    

    @staticmethod
    def _handle_sede(mapped_data):
        sede = Sede.objects.get(pk=mapped_data)
        return sede
    

    @classmethod    
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        print(mapped_data['sede'])
        sede = cls._handle_sede(mapped_data['sede'])
        return EquipoMedico.objects.create(
            id=mapped_data['id'],
            descripcion=mapped_data['descripcion'],
            tipo_equipo=mapped_data['tipo_equipo'],
            sede=sede,
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )