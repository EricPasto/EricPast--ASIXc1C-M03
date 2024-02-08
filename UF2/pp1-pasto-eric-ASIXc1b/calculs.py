"""
Eric Pastó
ASIX1B
28/03/2023
EXAMEN - calculs
"""
import SystemColors

def vocalsconsonants():
    print("vocalsconsonants\n")
    def calcularvocals():
        vocals = "aeiou"
        print("calculant vocals...")
    def calcularconsonants():
        print("calculant consonants...")

def lletres():
    def contar_lletres():
        caracters= [",",":","?","!",".",";",]
        paraula = input("text: ")
        contadorlletres = 0
        contadorcaracters = 0
        for x in paraula:
            if x == " ":
                contadorlletres = contadorlletres - 1
            elif x in caracters:
                contadorlletres = contadorlletres -1
            contadorlletres = contadorlletres + 1
            contadorcaracters = contadorcaracters + 1
        print("de", contadorcaracters, " caracters, hi ha ", contadorlletres, " lletres")
    contar_lletres()

def xifratgecesar():
    print("Xifratge Cèsar:\n")
    def calcularcesar():
        abecedari = {"a","b","c","d","f","g","h","i","j","k","l","m"
        ,"n","o","p","q","r","s","t","u","v","w","x","y","z"}
        paraula = input("text: ")
        cesar = ""
        for lletra in paraula:
            if lletra == abecedari:
                lletra = abecedari[+1]
                cesar.append(lletra)
        print(cesar)
    calcularcesar()

def colorsvocals():
    paraula = input("text: ")
    vocals = "aeiou"
    colors = [SystemColors.CVIOLET, SystemColors.CBLUE,
              SystemColors.CRED,SystemColors.CGREEN,
              SystemColors.CYELLOW]
    resultat = ""
    for l in paraula:
        if l.lower() in vocals:
            indice_vocal = vocals.index(l.lower())
            resultat = resultat + colors[indice_vocal] + l + SystemColors.CEND
        elif l.lower() not in vocals:
            resultat = resultat + l + SystemColors.CBLACK + SystemColors.CEND

    print(resultat)