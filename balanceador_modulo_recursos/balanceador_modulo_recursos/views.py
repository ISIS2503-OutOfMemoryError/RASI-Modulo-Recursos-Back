import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import balanceador_modulo_recurso_service as service
@csrf_exempt
def send_request(request):
    body = json.loads(request.body)
    path = request.path
    type = request.method
    #return JsonResponse({'response':'bien'}, status=200)
    response = service.execute_requests(body,path,type)
    return JsonResponse({'mensaje':'equipo creado correctamente'}, status=response.status_code)








