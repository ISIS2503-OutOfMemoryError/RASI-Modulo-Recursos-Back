import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import sede_logic  # Importa tu lógica de sede si es necesario

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def sede_create(request):
    if request.method == 'POST':
        try:
            # Intenta analizar los datos JSON de la solicitud
            data = json.loads(request.body)
            print(data)
            id = data.get('id')
            nombre = data.get('nombre')
            direccion = data.get('direccion')
            telefono = data.get('telefono')
            ciudad = data.get('ciudad')

            if nombre and direccion and telefono and ciudad:
                # Llama a la función create_sede con los datos validados
                sede = sede_logic.create_sede(id, nombre, direccion, telefono, ciudad)
                response_message = f'Se ha creado la sede "{nombre}" con éxito.'
                return JsonResponse({'message': response_message}, status=201)
            else:
                # Maneja el caso de datos faltantes o inválidos
                return JsonResponse({'error': 'Error en los datos enviados'}, status=400)
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST (por ejemplo, una solicitud GET)
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)

@csrf_exempt  # Esto es para deshabilitar la protección CSRF para fines de demostración
def sede_update(request):
    if request.method == 'PUT':
        try:
            # Intenta analizar los datos JSON de la solicitud
            data = json.loads(request.body)
            print(data)
            id = data.get('id')
            nombre = data.get('nombre')
            direccion = data.get('direccion')
            telefono = data.get('telefono')
            ciudad = data.get('ciudad')

            if nombre and direccion and telefono and ciudad:
                # Llama a la función create_sede con los datos validados
                sede = sede_logic.update_sede(id,nombre, direccion, telefono, ciudad)
                response_message = f'Se ha actualizado la sede "{nombre}" con éxito.'
                return JsonResponse({'message': response_message}, status=200)
            else:
                # Maneja el caso de datos faltantes o inválidos
                return JsonResponse({'error': 'Error en los datos enviados'}, status=400)
        except json.JSONDecodeError:
            print("JSONDecodeError")
            # Maneja el caso en el que la solicitud no contiene datos JSON válidos
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)

    # Maneja el caso en el que la solicitud no es un POST (por ejemplo, una solicitud GET)
    return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST'}, status=405)
