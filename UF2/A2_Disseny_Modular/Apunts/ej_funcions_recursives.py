"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""


# Funcions recursives
# Una funció recursiva és aquella que en executar-se fa anomenades a ella mateixa. Per tant hem de tenir “un cas basi” que fa acabar el bucle de crides. Vegem un exemple:

def factorial(numero):
    if (numero == 0 or numero == 1):

        return 1

    else:
        return numero * factorial(numero - 1)


factorial(5)
print(factorial(5))
# 120

# Orden de estructura, primero importar  bibliotecas y despues definicon de funciones y explicando
"""
from datatime import date
from datatime import datatime
from time import sleep
def obteneropcion():
    print("1. - Primera opció")
    print("2. - Millor opció")
    print("3. - Jo triaria aquesta")
    print("4. - La millor opció")
    print("5. - Sortir")
    return int(input())

def opcionprimera():
def opcionmillor():
def opcionJoTriariaAquesta():
def opcioLaMillor():
def tractarError(missatge):
def opcionfinal():
etc etc
Para mostrar el menu hacemos lo de abajo
opcio = obteOpcio()
while opcio != 5:...
    if opcio < 1 or opcio > 4:
        tractarError("opció no valida")

Finalizar
opcionfinal()
"""