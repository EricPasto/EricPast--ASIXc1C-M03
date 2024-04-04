"""
Eric Pastó
ASIX1B
04/04/2024
UF2 - pp1C - PetitesUtilitats
"""
vocals = ("a","e","i","o","u","A","E","I","O","U")

def contarVocalsiConsonants(nVocals=0, nConsonants=0):
    vocalsParaula = []
    consonantsParaula = []
    text = input("Introdueix el text: ")
    for l in text:
        if l in vocals:
            nVocals += 1
            vocalsParaula.append(l)
        else:
            nConsonants += 1
            consonantsParaula.append(l)
    print("Vocals   Quantitat   Consonants  Quantitat")
    print(f"{vocalsParaula} {nVocals}  {consonantsParaula} {nConsonants} ")

#contarVocalsiConsonants()