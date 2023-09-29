from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import sede_logic  # Importa tu lógica de sede si es necesario

def sede_create(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')

        if codigo and nombre and direccion and telefono and ciudad:
            # Llama a la función create_sede con los datos validados
            sede = sede_logic.create_sede(codigo, nombre, direccion, telefono, ciudad)

            # Redirige a una página de confirmación o muestra un mensaje de éxito
            return redirect('confirmacion_sede')  # Reemplaza 'confirmacion_sede' con tu URL de confirmación
        else:
            # Maneja el caso de datos faltantes o inválidos
            return HttpResponse('Error en los datos enviados')

    response_message = f'Se ha creado la sede "{sede.nombre}" con éxito.'
    return HttpResponse(response_message)

