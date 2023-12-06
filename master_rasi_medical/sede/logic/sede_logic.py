from ..models import Sede

def create_sede( id, nombre, direccion, telefono, ciudad):
    sede = Sede(id=id,nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad)
    sede.save()
    return sede

def update_sede(id,nombre, direccion, telefono, ciudad):
    sede = Sede.objects.get(id=id)
    sede.nombre = nombre
    sede.direccion = direccion
    sede.telefono = telefono
    sede.ciudad = ciudad
    sede.save()
    return sede







