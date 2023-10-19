import requests
from manage import ID_INSTANCIA as id_instancia

def crear_equipo_medico(data):
    try:
        #URL
        url = 'http://35.188.171.161:8080/equipo/crear_equipo/'
        #url = 'http://localhost:8080/equipo/crear_equipo/'
        #Body
        json = {"id" : id_instancia + 0.1,
                "body":data}
        #peticion
        response = requests.post(url, json=json)
        return response
    except:
        return "Error en la creacion del equipo medico"


    