from ..models import Sede

def create_sede(codigo, nombre, direccion, telefono, ciudad):
    sede = Sede(codigo=codigo, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad)
    sede.save()
    return sede

def update_sede(codigo, nombre, direccion, telefono, ciudad):
    sede = Sede.objects.get(codigo=codigo)
    sede.nombre = nombre
    sede.direccion = direccion
    sede.telefono = telefono
    sede.ciudad = ciudad
    sede.save()
    return sede







