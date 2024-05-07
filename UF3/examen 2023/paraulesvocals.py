"""
Eric Pastó
ASIX1B
02/5/2023
Examen
"""
"""
crea una copia del fitxer anomenat paraules.txt, 
afegint un numero que indiqui la quantitat de vocals de 
cadascuna de les paraules del fitxer, 
el fitxer resultant s'ha de dir paraulesQuantitatVocals.txt
"""
def copiar_i_afegir_vocals(arxiu_origen, arxiu_desti):
    # Obre l'arxiu d'origen en mode de lectura
    with open(arxiu_origen, 'r') as f:
        # Llegeix totes les línies de l'arxiu
        paraules = f.read().split()

    # Funció per calcular la quantitat de vocals en una paraula
    def contar_vocals(paraula):
        vocals = "aeiouAEIOU"
        return sum(1 for lletra in paraula if lletra in vocals)

    # Crea una llista de tuples amb la paraula i la quantitat de vocals
    paraules_vocals = [(paraula, contar_vocals(paraula)) for paraula in paraules]

    # Escriu al nou fitxer amb el número de vocals
    with open(arxiu_desti, 'w') as f_desti:
        for paraula, num_vocals in paraules_vocals:
            f_desti.write(f"{paraula} - {num_vocals} vocals\n")

# Crida a la funció per copiar i afegir la quantitat de vocals
#copiar_i_afegir_vocals("paraules.txt", "paraulesQuantitatVocals.txt")
