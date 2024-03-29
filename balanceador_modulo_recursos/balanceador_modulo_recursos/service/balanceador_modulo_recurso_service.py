import concurrent.futures
import requests

def execute_requests(body,path,type):
    urls = ["http://10.138.0.3:8080", "http://10.138.0.4:8080"]
    #Arreglar path
    url1 = urls[0] + path
    url2 = urls[1] + path
    urls = [url1,url2]
    #Realizar concurrencia de peticiónes
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(send_request, url,body,type): url for url in urls}
        
        # Espera hasta que se complete la primera tarea
        for future in concurrent.futures.as_completed(future_to_url):
            print("aca estoy")
            url = future_to_url[future]
            try:
                response = future.result()
                # Procesa la respuesta
                print(f"Respuesta de {url} recibida con estado {response.status_code}")
                return response  # Detiene el bucle después de la primera respuesta
            
            except Exception as exc:
                print(f"URL {url} generó una excepción: {exc}")
    return response

def execute_requests_get(path,type):
    urls = ["http://10.138.0.10:8080", "http://10.138.0.11:8080"]
    #Arreglar path
    url1 = urls[0] + path
    url2 = urls[1] + path
    urls = [url1,url2]
    #Realizar concurrencia de peticiónes
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(send_request, url,"",type): url for url in urls}
        # Espera hasta que se complete la primera tarea
        for future in concurrent.futures.as_completed(future_to_url):
            print("aca estoy")
            url = future_to_url[future]
            try:
                response = future.result()
                # Procesa la respuesta
                print(f"Respuesta de {url} recibida con estado {response.status_code}")
                return response  # Detiene el bucle después de la primera respuesta
            
            except Exception as exc:
                print(f"URL {url} generó una excepción: {exc}")
    return response


def send_request(url, body, type):
    if type == 'GET':
        response = requests.get(url)
    elif type == 'POST':
        response = requests.post(url, json=body)
    elif type == 'PUT':
        response = requests.put(url, json=body)
    return response
