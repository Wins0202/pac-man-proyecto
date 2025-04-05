"""JSON"""

import json 
import os

FILE_NAME = "records.json"

def load_or_initialize_json():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, KeyError):
            print("El archivo existe pero no contiene un JSON válido o no tiene la estructura esperada.")
    
    # Si no existe o no es válido, creamos estructura inicial
    initial_data = {"records": []}
    with open(FILE_NAME, 'w') as file:
        json.dump(initial_data, file, indent=4)
    return initial_data

    
def safeRecord (score):                 #Recibe como parametro un score
    records = load_or_initialize_json ()
    if records:
        if len(records) >= 3:           #Verificar si el array de records tiene 3 valores o más
            newRecords = records        #Guardar la variable la referencia de los records
            newRecords.pop()            #Elimina el ultimo puntaje y[0.0.x]
            newRecords.append(score)    #Agregando el nuevo score al json [y.0.0]

            records["records"] = newRecords  #Actualizando el array del json con el arrray modificado [y.0.0]
            
            with open (FILE_NAME, 'w') as fileW:     #Transcribe código de python a json y abrir el archivo pra poder modificarlo
                json.dump (records, file, indent=4)  #Mientras está abierto el archivo asignar los nuevos valores a json
        
        elif len(records) < 3:
            newRecords = records
            newRecords.append(score)
            records["records"] = newRecords
            with open (FILE_NAME, 'w') as file:     #Transcribe código de python a json y abrir el archivo pra poder modificarlo
                json.dump (records, file, indent=4)




