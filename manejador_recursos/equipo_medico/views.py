import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import equipo_medico_service as service

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def equipo_create(request):
    if request.method == 'POST':
        try:
            # Intenta analizar los datos JSON de la solicitud
            print(request.body)
            data = json.loads(request.body)
            #validar campos requeridos
            required_fields = ['id', 'descripcion', 'tipo_equipo', 'sede']
            for item in data:
                if item not in required_fields:
                    return JsonResponse({'error': f'Faltan campos'}, status=400)
                if data[item] == '':
                    return JsonResponse({'error': f'El campo {item} no puede estar vacío'}, status=400)
            #enviar peticion a la api
            respuesta = service.crear_equipo_medico(data)
            if respuesta.status_code == 201:
                return JsonResponse({'mensaje': 'Equipo creado correctamente'}, status=201)
            else:
                return JsonResponse(respuesta.text, status=respuesta.status_code, safe=False)
        
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST (por ejemplo, una solicitud GET)
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def equipo_update(request):
    if request.method == 'PUT':
        try:
            # Intenta analizar los datos JSON de la solicitud
            print(request.body)
            data = json.loads(request.body)
            #validar campos requeridos
            required_fields = ['id', 'descripcion', 'tipo_equipo', 'sede']
            for item in data:
                if item not in required_fields:
                    return JsonResponse({'error': f'Faltan campos'}, status=400)
                if data[item] == '':
                    return JsonResponse({'error': f'El campo {item} no puede estar vacío'}, status=400)
            #enviar peticion a la api
            respuesta = service.update_equipo_medico(data)
            if respuesta.status_code == 201:
                return JsonResponse({'mensaje': 'Equipo creado correctamente'}, status=201)
            else:
                return JsonResponse(respuesta.text, status=respuesta.status_code, safe=False)
        
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST (por ejemplo, una solicitud GET)
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes PUT'}, status=405)


