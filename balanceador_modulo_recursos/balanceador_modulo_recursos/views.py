import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import balanceador_modulo_recurso_service as service
@csrf_exempt
def send_request(request):
    if request.method == 'GET':
        path = request.path
        type = request.method
        response = service.execute_requests_get(path,type)
        dic = response.json()
        return JsonResponse(dic, status=response.status_code,safe=False)
    else:
        body = json.loads(request.body)
        path = request.path
        type = request.method
        response = service.execute_requests(body,path,type)
        return JsonResponse(response.json(), status=response.status_code)








