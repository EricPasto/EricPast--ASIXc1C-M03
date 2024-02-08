
def kcontar_vocales_02():
    try:
        noLetras = ["!", "¡", "?", "¿", ';', ',', ".", ":", "_", " "] #aqui estan las exepciones yade que si ve una de estos caracteres no lo tome en cuneta
        frase = input("texto=")
        txtvisto = {}#diccinario donde se guardara todas las posiciones  y la cantidad ademas de la propia letra
        for posicion, texto in enumerate(frase):
            if texto not in noLetras:#aqui lo que eh echo es que el for no solo lo haga de posicion si no tambien de texto ademas que 
            #la palabra enumerate no sabia que hacer ya de que un eln me daba error asi que acabe utlizando esto para enumerar la frase
                if texto not in txtvisto:#aqui utilizo la lista de expciones que no se tendran en cuneta
                    txtvisto[texto] = {'cantidad': 1, 'posiciones': [posicion]}
                else:
                    txtvisto[texto]['cantidad'] += 1
                    txtvisto[texto]['posiciones'].append(posicion)

        for letra in txtvisto:
            print(f'--Letras= {letra} --cantidad= {txtvisto[letra]["cantidad"]}  --posiciones= {txtvisto[letra]["posiciones"]}')
    except:
        print("Parece ser que el texto que ha introducido no ha funcionado. Vuelva a intentarlo de otra manera.")
