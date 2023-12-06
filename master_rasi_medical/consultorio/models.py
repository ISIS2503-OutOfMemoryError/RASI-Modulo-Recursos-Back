from django.db import models
from sede.models import Sede
from equipo_medico.models import EquipoMedico
from dj_cqrs.mixins import MasterMixin

class Consultorio(MasterMixin, models.Model):
    
    CQRS_ID = 'consultorio_model'

    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    #Esta realción es uno a uno, toca cabiarla uno a muchos
    #Es decir, un consultorio puede tener varios equipos médicos
    equipo_medico = models.ForeignKey(EquipoMedico, on_delete=models.CASCADE)   
    def __str__(self):  
        return self.nombre
