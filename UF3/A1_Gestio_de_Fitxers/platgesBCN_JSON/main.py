from platgesBCN import contar_playas_por_distrito

# Nombre del archivo JSON
archivo_json = 'opendatabcn_NP-NASIA_Platges-js.json'

# Llamar a la función y obtener el diccionario de número de playas por distrito
playas_por_distrito = contar_playas_por_distrito(archivo_json)

# Imprimir el número de playas por distrito
print("Número de playas por distrito:")
for distrito, num_playas in playas_por_distrito.items():
    print(f"{distrito}: {num_playas} playas")
