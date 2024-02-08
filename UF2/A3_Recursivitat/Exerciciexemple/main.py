
#primero crearemos una definicion donde se pedira los otros archivo 
#ejemplo cundo le des a Utilitat Estaditiques haremos un import del archivo de submenu para asi ejecute lo que tiene dentro 
# le pondremos un pequeña frase para que eleija la opcion en el print (1-Utilitat Estadistiques)
from archivo1 import *
from archivo2 import *
from archivo3 import *
from archivo4 import *
from colores import *

# Define la función del menú
def Menu():
    try:
        print("1 - contador de caracteres")
        print("2 - contador de vocales y consonantes")
        print("3 - encriptar palabras")
        print("4 - colorear vocales")
        print("5 - salir")
        opcion = int(input("OPCION= "))
        if opcion == 1:
            kcontar_letras_01()
            Menu()
        elif opcion == 2:
            kcontar_vocales_02()
            Menu()
        elif opcion == 3:
            Kconvertir_ASCII_03()
            Menu()
        elif opcion == 4:
            Kcolorear_vocales_04()
            Menu()
        else: 
            opcion == 5
            print("muy bein acabas de salir")
    except ValueError:
        print("Error: Debe ingresar un valor numérico")
        Menu()

Menu()





