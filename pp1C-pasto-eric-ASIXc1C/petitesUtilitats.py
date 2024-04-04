"""
Eric Pastó
ASIX1B
04/04/2024
UF2 - pp1C - PetitesUtilitats
"""

import codificar_text
import colors_vocals
import posicio_signes_puntuacio
import quantitat_signes_puntuacio
def menu():
    demanar = input("1-Signes puntuació - Quantitat \n" "2-Signes de puntuació - Posició \n"  "3-Text - Codificar \n" "4-Text - Colors Vocals \n" "5-Executar tot \n" "6-Sortir de l'aplicació\n" "\n : ")
    if demanar == '1':
        quantitat_signes_puntuacio.frase()
    elif demanar == "2":
        posicio_signes_puntuacio.contarVocalsiConsonants()
    elif demanar == "3":
        codificar_text.codificar()
    elif demanar == "4":
        colors_vocals.colorejarVocalsiConsonants()
    elif demanar == "5":
        quantitat_signes_puntuacio.frase(),
        posicio_signes_puntuacio.contarVocalsiConsonants(),
        codificar_text,
        colors_vocals.colorejarVocalsiConsonants()
    elif demanar == "6":
        print("Sortint de la aplicació...")
    else:
        print("Error, indica una de les opcions indicades.")
        menu()

menu()
