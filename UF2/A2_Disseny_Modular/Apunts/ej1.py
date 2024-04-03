"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""
import random

print(random.randint(1, 10))


#Pots importar un mòdul i assignar-lo a un nom diferent:


import random as rdm

print(rdm.randint(1, 10))



#Importar una funció
#També és possible importar una funció d'un mòdul:

from math import sin

sin(1) #0.8414709848078965





#Importar tots els noms d'un mòdul
from module_name import *

#Per exemple

from math import *

sqrt(2) # instead of math.sqrt(2)

ceil(2.7) # instead of math.ceil(2.7)



#En quin ordre importar els mòduls
#Ordena les importacions de la següent manera a la part superior del mòdul:

#1Importació de la biblioteca estàndard

#2Importacions de tercers

#3Importacions específiques de l'aplicació/biblioteca local

#La mejor opcion de modulo es
# Escribir import modu y ya esta
# Y sino escribir from modu import sqrt