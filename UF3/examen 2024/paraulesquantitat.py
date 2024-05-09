"""
Eric Pastó
ASIXc1C

Examen UF3
"""
"""
Crea un fitxer amb la quantitat de paraules que comencen per cada lletra
"""
import os
def copiar_i_afegir_lletres(arxiu_origen, arxiu_desti):


    # Obre l'arxiu d'origen en mode de lectura
    with open(arxiu_origen, 'r') as f:
        # Llegeix totes les línies de l'arxiu
        paraules = f.read().split()

    # Funció per calcular la quantitat de lletres en una paraula
    def contar_lletres(paraula):
        lletres = "qwertyuiopasdfghjklñçzxcvbnmQWERTYUIOPASDFGHJKLKÑÇZXCVBNM"
        return sum(1 for lletra in paraula if lletra in lletres)

    # Crea una llista de tuples amb la paraula i la quantitat de lletres
    paraules_vocals = [(paraula, contar_lletres(paraula)) for paraula in paraules]

    # Escriu al nou fitxer amb el número de lletres
    with open(arxiu_desti, 'w') as f_desti:
        for paraula, num_lletres in paraules_vocals:
            f_desti.write(f"{paraula} - {num_lletres} lletres\n")