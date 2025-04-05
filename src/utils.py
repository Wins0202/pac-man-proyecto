"""JSON"""

import json 
import os

SRC_DIR = os.path.join(os.path.dirname(__file__), '')
FILE_NAME = os.path.join(SRC_DIR, "records.json")

def load_or_initialize_json():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, KeyError):
            print("El archivo existe pero no contiene un JSON válido o no tiene la estructura esperada.")
    
    initial_data = {"records": []}
    with open(FILE_NAME, 'w') as file:
        json.dump(initial_data, file, indent=4)
    return initial_data

    
def safeRecord (score):                 #Recibe como parametro un score
    data = load_or_initialize_json ()
    records = data["records"]
    if len(records) >= 3:           #Verificar si el array de records tiene 3 valores o más
        newRecords = records        #Guardar la variable la referencia de los records
        newRecords.pop()            #Elimina el ultimo puntaje y[0.0.x]
        newRecords.insert(0, score)    #Agregando el nuevo score al json [y.0.0]

        data["records"] = newRecords  #Actualizando el array del json con el arrray modificado [y.0.0]
        
        with open (FILE_NAME, 'w') as fileW:     #Transcribe código de python a json y abrir el archivo pra poder modificarlo
            json.dump (data, fileW, indent=4)  #Mientras está abierto el archivo asignar los nuevos valores a json
    
    if len(records) < 3:
        newRecords = records
        newRecords.insert(0, score)
        data["records"] = newRecords
        with open (FILE_NAME, 'w') as fileW :     #Transcribe código de python a json y abrir el archivo pra poder modificarlo
            json.dump (data, fileW, indent=4)