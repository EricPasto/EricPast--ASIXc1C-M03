"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""
#Definició de funcions d'usuari

def greet():

   print("Hello")



def greetTwo(greeting):

   print(greeting)



# Crida a la funció definida prèviament

greet()

#Crida d'una altra funció amb un argument/paràmetre

greetTwo("Bon dia tingui i no s'entretingui")

#Variables Locals
#L'àmbit d'una variable és el lloc en el codi font on aquesta variable es pot usar.
# Una variable local que es declaren dins d'una funció no es poden utilitzar fora d'aquesta funció.

def operar(a,b):

   suma = a + b

   resta = a - b	# La variable "resta" és d'àmbit local a la funció "operar"

   print(suma,resta)



operar(4,5)

#resta #NameError: name 'resta' is not defined

#Variables globals
#Podem definir variables globals, que seran visibles en tot el mòdul.
# Es recomana declarar-les en majúscules:

PI = 3.1415

def area(radio):

   return PI*radio**2



area(2) # 12.566