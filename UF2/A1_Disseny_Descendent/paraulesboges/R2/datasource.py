"""
Eric Pastó
Aleix de Diego
Erik Nuñez
ASIX1B
20/2/2023
ParaulesBojes -R2
"""
import requests
from paraulesboges import *
from main import *
def getDataFromKeyboard():
    paraulesboges.text = input("Escriu la frase per teclat: ")
    paraulesboges.frasealeatoria = paraulesboges.fer_aleatories(paraulesboges.text)
    print(paraulesboges.frasealeatoria)