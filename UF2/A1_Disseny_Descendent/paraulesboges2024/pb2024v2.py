def fer_aleatories():
    with open("paraules.txt", "r") as f:
        text = f.read()

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

    with open("boges.txt", "w") as f:
        f.write(' '.join(paraulesboges))


fer_aleatories()