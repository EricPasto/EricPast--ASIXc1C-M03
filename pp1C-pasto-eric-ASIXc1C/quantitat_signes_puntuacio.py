"""
Eric Pastó
ASIX1B
04/04/2024
UF2 - pp1C - PetitesUtilitats
"""
def frase():
    acabat = "false"
    frase = []

    try:
        while acabat != "true":
            fraseseparada=input("Introdueix el text: ").split()
            frase.append(fraseseparada)
            if fraseseparada[0] == "q":
                print("Finalitzant el programa...")
                acabat = "true"
                return acabat
            return fraseseparada

    except:
        print("Error - El que has introduit es incorrecte")


#frase()
