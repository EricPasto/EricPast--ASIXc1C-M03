import json

def contar_playas_por_distrito(archivo_json):
    # Diccionario para almacenar el número de playas por distrito
    playas_por_distrito = {}

    # Leer el archivo JSON y contar las playas por distrito
    with open(archivo_json, 'r') as f:
        datos = json.load(f)
        for elemento in datos:
            for direccion in elemento['addresses']:
                if 'district_name' in direccion:
                    nombre_distrito = direccion['district_name']
                    # Si el distrito ya está en el diccionario, incrementa el contador
                    if nombre_distrito in playas_por_distrito:
                        playas_por_distrito[nombre_distrito] += 1
                    # Si no, agrega el distrito al diccionario y establece el contador en 1
                    else:
                        playas_por_distrito[nombre_distrito] = 1

    # Retorna el diccionario con el número de playas por distrito
    return playas_por_distrito


