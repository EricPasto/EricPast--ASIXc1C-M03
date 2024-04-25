import pandas
import csv

FILE_NAME = "2023_03_Marc_BicingNou_INFORMACIO.csv"
def encontrar_estaciones(FILE_NAME):
    # Inicializamos la capacidad máxima y la estación correspondiente
    capacidad_maxima = 0
    estacion_maxima = None
    capacidad_minima = float('inf')
    estacion_minima = None

    # Abrimos el archivo CSV
    with open(FILE_NAME, newline='') as archivo:
        lector_csv = csv.reader(archivo)

        # Saltamos la primera fila si contiene encabezados
        encabezados = next(lector_csv, None)

        # Iteramos sobre las filas del archivo
        for fila in lector_csv:
            # Obtenemos la capacidad de la estación de la fila actual
            capacidad_estacion = int(fila[8])  # Suponiendo que la capacidad está en la segunda columna

            # Comparamos la capacidad actual con la máxima encontrada hasta ahora
            if capacidad_estacion > capacidad_maxima:
                capacidad_maxima = capacidad_estacion
                estacion_maxima = fila[1]  # Suponiendo que el nombre de la estación está en la primera columna

            if capacidad_estacion < capacidad_minima:
                capacidad_minima = capacidad_estacion
                estacion_minima = fila[1]

    # Devolvemos la estación con la capacidad máxima
    return (estacion_maxima,capacidad_maxima), (estacion_minima, capacidad_minima)


# Llamamos a la función para encontrar la estación con más capacidad
estacion_maxima, estacion_minima = encontrar_estaciones(FILE_NAME)

# Imprimimos el resultado
if estacion_maxima:
    print(f"La estación con más capacidad es '{estacion_maxima[0]}' con una capacidad de {estacion_maxima[1]} bicicletas.")
else:
    print("No se encontraron estaciones en el archivo CSV.")

if estacion_minima:
    print(f"La estación con menos capacidad es '{estacion_minima[0]}' con una capacidad de {estacion_minima[1]} bicicletas.")
else:
    print("No se encontraron estaciones en el archivo CSV.")