"""
Eric Pastó

Examen UF3
"""
"""
crea 5 fitxers per guardar les paraules que acaben en: 
ing,itb,tic,tica i ció
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

    # Crea fitxers per a cada cua de paraula especificada
    for cua in ["ing", "itb", "tic", "tica", "ció"]:
        # Filtra les paraules amb la cua actual
        paraules_filtrades = [paraula for paraula in paraules if cua in paraula]
        # Crea el nom del fitxer de sortida
        nom_fitxer_sortida = os.path.join(carpeta_sortida, f"{prefixe_fitxer_sortida}_{cua}.txt")
        # Escriu les paraules filtrades al fitxer de sortida
        with open(nom_fitxer_sortida, 'w') as f_sortida:
            for paraula in paraules_filtrades:
                f_sortida.write(f"{paraula}\n")