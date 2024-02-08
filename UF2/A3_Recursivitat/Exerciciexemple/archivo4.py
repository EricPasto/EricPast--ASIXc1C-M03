from colores import *

def Kcolorear_vocales_04():
    palabra = input("texto=")
    vocales = "aeiou"
    colores = [CBLACK, CBLUE, CRED, CGREEN, CYELLOW]
    resultado = ""

    for letra in palabra:
        if letra.lower() in vocales:
            indice_vocal = vocales.index(letra.lower())
            resultado += colores[indice_vocal] + letra + CRESET
        else:
            resultado += letra

    print(resultado)

