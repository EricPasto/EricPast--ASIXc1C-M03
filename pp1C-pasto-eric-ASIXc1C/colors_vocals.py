"""
Eric Pastó
ASIX1B
04/04/2024
UF2 - pp1C - PetitesUtilitats
"""
import systemColors


vocals = ("a","e","i","o","u","A","E","I","O","U")
colors={
    "RED": systemColors.CRED,
    "BLUE": systemColors.CBLUE,
    "YELLOW": systemColors.CYELLOW,
    "BLACK": systemColors.CBLACK,
    "WHITE": systemColors.CWHITE,
    "VIOLET": systemColors.CVIOLET,
    "GREEN": systemColors.CGREEN}
def colorejarVocalsiConsonants():
    vocalsParaula = []
    consonantsParaula = []
    text = input("Introdueix el text: ")
    for l in text:
        if l in vocals:
            vocalsParaula.append(l)
        else:
            consonantsParaula.append(l)

    print(f" {systemColors.CRED} {vocalsParaula}, {systemColors.CBLACK} {consonantsParaula}  ")


#colorejarVocalsiConsonants()