"""
Eric Pastó
ASIX1B
28/2/2023
RGBRectangles
"""

import SystemColors

llista=[]
colors={
    "RED": SystemColors.CRED,
    "BLUE": SystemColors.CBLUE,
    "YELLOW": SystemColors.CYELLOW,
    "BLACK": SystemColors.CBLACK,
    "WHITE": SystemColors.CWHITE,
    "VIOLET": SystemColors.CVIOLET,
    "GREEN": SystemColors.CGREEN
}
#Escrui l'imput i afegeix les dades a una llista

rectangle = input()
paraules = rectangle.split()
for p in paraules:
    llista.append(p)
#defineix ample i llarg
ample = int(paraules[1])
llarg = int(paraules[2])

#Realitza el rectangle amb el color i mida especificada
def forma():
    try:
        for i in range(ample):
            for l in range(llarg):
                print(colors[paraules[0].upper()]+ "x ", end="")
            print("")
    except:
        print("El color que acabas de introducir no esta en la lista")


forma()