from django.db import models
from sede.models import Sede
from dj_cqrs.mixins import MasterMixin

class EquipoMedico(MasterMixin, models.Model):

    CQRS_ID = 'equipo_medico_model'

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
    def __str__(self):
        return self.tipo_equipo
