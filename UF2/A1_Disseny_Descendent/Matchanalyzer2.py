"""
Eric Pastó
ASIXc1C
7/2/2024
MatchAnalizer
"""
#demanar equips
equipA = ""
equipB = ""
marcadorA = [0]
marcadorB = [0]
def llegirequips():
    equipA=input("Nom de l'equip 1: ")
    equipB=input("Nom de l'equip 2: ")
    return equipA, equipB
def comentar_jugades():
    #EquipB
    for i in range(len(marcadorB)-1):
        if marcadorB[i+1]-marcadorB[i] ==2:
            print("Canasta de "+equipB)
        elif marcadorB[i+1]-marcadorB[i] ==1:
            print("Tir lliure de "+equipB)
        elif marcadorB[i+1]-marcadorB[i] ==3:
            print("Triple de "+equipB)
    #EquipA
    for i in range(len(marcadorA)-1):
        if marcadorA[i+1]-marcadorA[i] ==2:
            print("Canasta de "+equipA)
        elif marcadorA[i+1]-marcadorA[i] ==1:
            print("Tir lliure de "+equipA)
        elif marcadorA[i+1]-marcadorA[i] ==3:
            print("Triple de "+equipA)

def hem_acabat(punts):
    acabat = False
    if punts[0] == "-1":
        acabat = True
    return acabat
def qui_guanya():
    guanyador = ""
    if marcadorA[-1] > marcadorB[-1]:
        guanyador = equipA
    elif marcadorB[-1] > marcadorA[-1]:
        guanyador = equipB
    return guanyador

def llegiranotacions(punts=None):
    try:
        punts = input(": ").split(" ")
        while not hem_acabat(punts):
            marcadorA.append(int(punts[0]))
            marcadorB.append(int(punts[1]))
            punts=input(": ").split(" ")
    except:
        print("Posa numeros!")

equipA, equipB = llegirequips()
llegiranotacions()
guanyador=qui_guanya()
comentar_jugades()

if guanyador != "":
    print(f"El guanyador es: {guanyador}")
else:
    print("Empat!")
