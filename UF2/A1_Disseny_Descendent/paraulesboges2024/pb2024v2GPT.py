import random
def fer_aleatories():
    text = input("Introduce el texto: ")

    paraules = text.split()
    paraulesboges = []
    caractersespecials = [",", ".", "?", "¿", "'", "!", "¡", ":", ";"]

    for p in paraules:
        if len(p) <= 3:
            paraulesboges.append(p)
        elif p[-1] in caractersespecials:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-2], len(p) - 3)) + p[-2] + p[-1])
        else:
            paraulesboges.append(p[0] + ''.join(random.sample(p[1:-1], len(p) - 2)) + p[-1])

    resultat = ' '.join(paraulesboges)
    print(resultat)
    print("Es a dir: ")
    print(text)
    return resultat

fer_aleatories()
