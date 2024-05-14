from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.shortcuts import render

def read_json_file(request):
    # Ruta al archivo JSON (por ejemplo, dentro del directorio de medios)
    json_file_path = 'event_log/static/oneday_data.json'

    # Intentar abrir y leer el archivo JSON
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            # Obtener las primeras keys del diccionario
            primeras_keys = list(data.keys())  # Obtener las primeras 2 keys, por ejemplo

            print("Las primeras keys del JSON son:", primeras_keys)
            for key in primeras_keys:
              print(key)
              # Obtener el valor asociado a la key
              value = data[key]
              sub_keys =  list(value.keys())
              list_aux = []
              for sub_key in  sub_keys:  # Ordenar keys como enteros y obtener los primeros 5
                sub_dict = value[sub_key]
                if key!="context" and key!="username" and  key!="session" and  key!="referer" and  key!="event" and  key!="time" and key!="event_type" and key!="page" and key!="agent":
                  if sub_dict not in list_aux:      
                    list_aux.append(sub_dict)
                # print(f"Primeros 5 elementos de '{key}[{sub_key}]': {sub_dict}")
              print(list_aux)  
            # Devolver los datos leídos como una respuesta JSON
            data = {
                  'key1': 'value1',
                  'key2': 'value2',
                  'list_key': list_aux
            }

            return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({'error': 'Archivo JSON no encontrado'}, status=404)
