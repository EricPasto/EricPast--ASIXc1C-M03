"""
Eric Pastó
Aleix de Diego
Erik Nuñez
ASIX1B
20/2/2023
ParaulesBojes -R2
"""

import random
def fer_aleatories(text):
    paraules = text.split()
    paraulesboges = []
    caractersespecials = [",", ".", "?", "¿", "'", "!", "¡", ":", ";"]
    for p in paraules:
        if len(p) <= 3:
            paraulesboges.append(p)
        elif p[-1] in caractersespecials:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-2], len(p)-3)) + p[-2] + p[-1])
        else:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-1], len(p)-2)) + p[-1])
    return ' '.join(paraulesboges)

#text = input("")
#frasealeatoria = fer_aleatories(text)
#print(frasealeatoria)