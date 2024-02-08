"""
Eric Pastó
Aleix de Diego
Erik Nuñez
ASIX1B
20/2/2023
ParaulesBojes -R2
"""
import random
#definicions
def fer_aleatories(text):
    paraules = text.split()
    paraulesboges = []
    caractersespecials = [",", ".", "?", "¿", "'", "!", "¡", ":", ";"]
    for p in paraules:
        if len(p) <= 3:# control d'errors, si la paraula te menys de 3 lletres no cambia l'ordre
            paraulesboges.append(p)
        elif p[-1] in caractersespecials:# si la paraula acaba en caracter especial, no el desordena.
            paraulesboges.append(p[0] + p[-2:1:-1] + p[-2] + p[-1])
        else:
# Afegir la primera i ultima lletra de cada paraula desordenada
            paraulesboges.append(p[0] + p[-2:0:-1] + p[-1])
# Uneix en una cadena les paraules
    return ' '.join(paraulesboges)

#execució
text = input("")
frasealeatoria = fer_aleatories(text)
print(frasealeatoria)