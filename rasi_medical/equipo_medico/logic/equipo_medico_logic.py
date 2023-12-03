from ..models import EquipoMedico

def create_equipo(id,descripcion,tipo_equipo,sede):
    equipo = EquipoMedico(
        id = id,
        descripcion = descripcion,
        tipo_equipo = tipo_equipo,
        sede = sede
    )
    equipo.save()
    return equipo

def update_equipo(id,descripcion,tipo_equipo,sede):
    equipo = EquipoMedico.objects.get(id=id)
    if(equipo != None):
        equipo.descripcion = descripcion
        equipo.tipo_equipo = tipo_equipo
        equipo.sede = sede
        equipo.save()
    return equipo

def get_equipos():
    equipos = EquipoMedico.objects.all()
    return equipos
