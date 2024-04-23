import json
# Nombre del archivo JSON
archivo_json = "opendatabcn_NP-NASIA_Platges-js.json"

# Función para encontrar todas las "district_name"
def encontrar_district_names(archivo_json):
    with open('opendatabcn_NP-NASIA_Platges-js.json', "r") as f:
        data = json.load(f)
        district_names = set()  # Usamos un conjunto para evitar duplicados
        # Recorremos los elementos del JSON
        for elemento in data:
            if "district_name" in elemento:  # Comprobamos si la clave existe en el elemento
                district_names.add(elemento["district_name"])
    return district_names

# Llamamos a la función e imprimimos los resultados
district_names = encontrar_district_names('opendatabcn_NP-NASIA_Platges-js.json')
print("District Names encontrados:")
for name in district_names:
    print(name)