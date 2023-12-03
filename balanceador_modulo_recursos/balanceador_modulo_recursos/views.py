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
    response = service.execute_requests_get(path,type)
    return JsonResponse({'mensaje':'petición enviada'}, status=response.status_code)








