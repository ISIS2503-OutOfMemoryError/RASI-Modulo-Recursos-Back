import requests
from manage import ID_INSTANCIA as id_instancia
import time

def crear_equipo_medico(data):
    try:
        #URL
        url = 'http://10.138.0.6:8080/equipo/crear_equipo/'
        #url = 'http://localhost:8080/equipo/crear_equipo/'
        #Body
        json = {"id" : id_instancia + 0.1,
                "body":data}
        #peticion
        response = requests.post(url, json=json)

        if response.status_code == 401:
            time.sleep(2)

        return response
    except:
        return "Error en la creacion del equipo medico"
    
def update_equipo_medico(data):
    try:
        #URL
        url = 'http://10.138.0.6:8080/equipo/put_equipo/'
        #url = 'http://localhost:8002/equipo/put_equipo/'
        #Body
        json = {"id" : id_instancia + 0.1,
                "body":data}
        #peticion
        response = requests.put(url, json=json)
        return response
    except:
        return "Error en la creacion del equipo medico"
    

def get_equipos_medicos():
    try:
        #URL
        url = 'http://10.138.0.2:8080/equipo/equipos/'
        #url = 'http://localhost:8002/equipo/equipos/'
        #peticion
        response = requests.get(url)
        return response
    except:
        return "Error en la obtencion de los equipo medico"




    