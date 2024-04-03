import random
import requests

cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
Texto_Ordenado = []
palabras = []
frase_Desordenado = []

def obtener_texto_desde_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error - No se pudo obtener el texto de la URL.")
            return None
    except Exception as e:
        print("Error -", e)
        return None

def frase():
    try:
        texto = obtener_texto_desde_url("https://example-files.online-convert.com/document/txt/example.txt")
        if texto:
            frase_ordenada = texto.split()
            return frase_ordenada, texto
        else:
            return None, None
    except:
        print("Error - Lo que has introducido es incorrecto")
        return None, None

def separar():
    for palabrades in Texto_Ordenado:
        if len(palabrades) >= 3:
            if palabrades[-1] in frase and palabrades[-1] not in cEspeciales:
                sep = list(palabrades[1:-1])
                random.shuffle(sep)
                separado = palabrades[0] + ''.join(sep) + palabrades[-1]
            elif palabrades[-1] in cEspeciales:
                sep = list(palabrades[1:-2])
                random.shuffle(sep)
                separado = palabrades[0] + ''.join(sep) + palabrades[-2] + palabrades[-1]
        else:
            separado = palabrades
        palabras.append(separado)
    return palabras

def juntar():
    frasedes = ' '.join(palabras)
    return frasedes

def resultado():
    print(frase_Desordenado)
    print("Texto ordenado:")
    print(frase)

Texto_Ordenado, frase_Desordenado = frase()
if Texto_Ordenado:
    palabras = separar()
    print(juntar())