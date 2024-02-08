"""
Eric Pastó
ASIX1B
21/03/2023
UF1 - PetitesUtilitats
"""
import Utilitats_estadistiques
import Utilitats_cadenes
def menu():
    demanar = input(" 1-Utilitats Estadistiques\n 2-Utilitats de Cadenes\n 3-Sortir de l'aplicació\n : ")
    if demanar == '1':
        submenu1()
    elif demanar == "2":
        submenu2()
    elif demanar == "3":
        print("Sortint de la aplicació...")
    else:
        print("Error, indica una de les opcions indicades.")
        menu()
def submenu1():
    demanar = input(" 1.1-Calcular mitjana\n 1.2-Calcular mediana\n 1.3-Calcular desviació estàndard\n 1.4-Tornar al menú anterior\n : ")
    if demanar == '1':
        Utilitats_estadistiques.calculo_mitjana()
        submenu1()
    elif demanar == "2":
        Utilitats_estadistiques.calculo_mediana()
        submenu1()
    elif demanar == "3":
        Utilitats_estadistiques.calculo_desviestandard()
        submenu1()
    elif demanar == "4":
        menu()
    else:
        print("Error, indica una de les opcions indicades.")
        submenu1()
def submenu2():
    demanar = input(" 2.1-CrazyWords\n 2.2-Es una frase palindroma?\n 2.3-Xifratge de Cèsar\n 2.4-Tornar al menú anterior\n : ")
    if demanar == '1':
        print("Escriu la frase a desordenar: ")
        Utilitats_cadenes.crazywords()
        submenu2()
    elif demanar == "2":
        Utilitats_cadenes.frasepalindroma()
        submenu2()
    elif demanar == "3":
        Utilitats_cadenes.xifratgecesar()
        submenu2()
    elif demanar == "4":
        menu()
    else:
        print("Error, indica una de les opcions indicades.")
        submenu2()
menu()