"""
Eric Pastó
"""
"""
crea 5 fitxers per guardar les paraules que tenen 2, 4, 6, 8 i 10 
caracters d'un arxiu anomenat paraules.txt
"""
import os

def guardar_paraules_per_longitud(arxiu_origen, prefixe_fitxer_sortida, carpeta_sortida):
    # Comprova si la carpeta de sortida existeix, si no, la crea
    if not os.path.exists(carpeta_sortida):
        os.makedirs(carpeta_sortida)

    # Obre l'arxiu d'origen en mode de lectura
    with open(arxiu_origen, 'r') as f:
        # Llegeix totes les línies de l'arxiu
        paraules = f.read().split()

    # Crea fitxers per a cada longitud de paraula especificada
    for longitud in [2, 4, 6, 8, 10]:
        # Filtra les paraules amb la longitud actual
        paraules_filtrades = [paraula for paraula in paraules if len(paraula) == longitud]
        # Crea el nom del fitxer de sortida
        nom_fitxer_sortida = os.path.join(carpeta_sortida, f"{prefixe_fitxer_sortida}_{longitud}.txt")
        # Escriu les paraules filtrades al fitxer de sortida
        with open(nom_fitxer_sortida, 'w') as f_sortida:
            for paraula in paraules_filtrades:
                f_sortida.write(f"{paraula}\n")

# Crida a la funció per desar les paraules per longitud
#guardar_paraules_per_longitud("paraules.txt", "paraules_longitud", "sortida")

