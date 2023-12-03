import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import equipo_medico_logic  # Importa tu lógica de sede si es necesario
from django.core.serializers import serialize
from sede.models import Sede
# Declarar la variable lo como global fuera de la función
from manage import lock_out
import time

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def equipo_create(request):
    global lock_out
    if request.method == 'POST':
        try:
            # Intenta analizar los datos JSON de la solicitud
            data = json.loads(request.body)
            id = data.get('id')
            body = data.get('body')
            #Voting
            print(lock_out)
            if lock_out==0:
                print("Voto aceptado")
                lock_out=id
            else:
                #Retorna el candado a estado neutro
                time.sleep(0.1)
                lock_out=0
                return JsonResponse({'error':'error aceptación petición'}, status=401)
            
            #Cuerpo del equipo
            id = body.get('id')
            descripcion = body.get('descripcion')
            tipo_equipo = body.get('tipo_equipo')
            sede_data = body.get('sede')
            #Relación sede
            sede = Sede(
            id=sede_data.get('id'),
            nombre=sede_data.get('nombre'),
            direccion=sede_data.get('direccion'),
            telefono=sede_data.get('telefono'),
            ciudad=sede_data.get('ciudad'))

            if descripcion and tipo_equipo and sede and id:
                # Llama a la función create_sede con los datos validados
                equipo = equipo_medico_logic.create_equipo(id, descripcion, tipo_equipo, sede)
                response_message = f'Se ha creado el equipo "{id}" con éxito.'
                return JsonResponse({'message': response_message}, status=201)
            else:
                # Maneja el caso de datos faltantes o inválidos
                print("Error en los datos enviados")
                return JsonResponse({'error': 'Error en los datos enviados'}, status=400)
        
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def equipo_update(request):
    global lock_out
    if request.method == 'PUT':
        try:
            # Intenta analizar los datos JSON de la solicitud
            data = json.loads(request.body)
            id = data.get('id')
            body = data.get('body')
            #Voting
            print(lock_out)
            if lock_out==0:
                print("Voto aceptado")
                lock_out=id
            else:
                #Retorna el candado a estado neutro
                time.sleep(0.1)
                lock_out=0
                return JsonResponse({'error':'error aceptación petición'}, status=401)
            
            #Cuerpo 
            id = body.get('id')
            descripcion = body.get('descripcion')
            tipo_equipo = body.get('tipo_equipo')
            sede_data = body.get('sede')
            #Relación sede
            sede = Sede(
            id=sede_data.get('id'),
            nombre=sede_data.get('nombre'),
            direccion=sede_data.get('direccion'),
            telefono=sede_data.get('telefono'),
            ciudad=sede_data.get('ciudad'))

            if descripcion and tipo_equipo and sede and id:
                # Llama a la función create_sede con los datos validados
                equipo = equipo_medico_logic.update_equipo(id, descripcion, tipo_equipo, sede)
                response_message = f'Se ha actualizado el equipo "{id}" con éxito.'
                return JsonResponse({'message': response_message}, status=200)
            else:
                # Maneja el caso de datos faltantes o inválidos
                print("Error en los datos enviados")
                return JsonResponse({'error': 'Error en los datos enviados'}, status=400)
            
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)


#Get equipos 
@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def equipos_get(request):
    global lock_out
    if request.method == 'GET':
        # Intenta analizar los datos JSON de la solicitud
        id = 1
        #Voting
        print(lock_out)
        if lock_out==0:
            print("Voto aceptado")
            lock_out=id
        else:
            #Retorna el candado a estado neutro
            time.sleep(0.1)
            lock_out=0
            return JsonResponse({'error':'error aceptación petición'}, status=401)
        
        # Llama a la función create_sede con los datos validados
        equipos = equipo_medico_logic.get_equipos()
        print(equipos)
        return JsonResponse(equipos,safe=False, status=200)
    # Maneja el caso en el que la solicitud no es un POST
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)

