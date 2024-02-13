"""
Eric Pastó
ASIXc1C
08/02/2024
MatchAnalizer - Volem fer un programa que analitzi els resultats d'un partit de bàsquet.
Tenir en compte que en un partit de bàsquet es poden fer 1, 2 o 3 punts.
Donat els diferents resultats analitza que està passant.
L'usuari introduirà primer el nom dels dos equips i després el resultat actual
"""

equip1 = ""
equip2 = ""
puntse1 = 0
puntse2 = 0

#obtenirEquips
def obtenirEquips():
    equip1 = print (input ("Nom de l'equip 1? "))
    equip2 = print (input ("Nom de l'equip 2? "))
    return equip1, equip2
#obtenir resultats
def obtenirResultats():
    print("hola")
#procesar resultats
#tractar errors

obtenirEquips()
print ("els equips son: ",equip1, equip2)