"""
Eric Pastó
ASIX1B
28/03/2023
EXAMEN - main
"""
import calculs
def menu():
    demanar = input(" 1-Calcular lletres\n 2-Calcular vocals i consonants\n 3-Xifratge Cèsar\n 4-Colorejar vocals\n 5-Sortir de l'aplicació\n: ")
    if demanar == '1':
        calculs.lletres()
        menu()
    elif demanar == "2":
        calculs.vocalsconsonants()
        menu()
    elif demanar == "3":
        calculs.xifratgecesar()
        menu()
    elif demanar == "4":
        calculs.colorsvocals()
        menu()
    elif demanar == "5":
        print("Sortint de la aplicació...")
    else:
        print("Error, indica una de les opcions indicades.")
        menu()
menu()