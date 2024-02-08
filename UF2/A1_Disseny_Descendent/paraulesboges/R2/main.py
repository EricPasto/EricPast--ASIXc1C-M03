"""
Eric Pastó
Aleix de Diego
Erik Nuñez
ASIX1B
20/2/2023
ParaulesBojes -R2
"""
import openai
openai.api_key ="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"
import paraulesboges

opcio = []
def menu():
    demanar = input("Chatgpt(C), Teclat(T), Link(L): ")
    if demanar == 'T':
        opcio.append("teclat")
    elif demanar == "L":
        opcio.append("link")
    elif demanar == "C":
        opcio.append("chatgpt")
    else:
        print("Error, indica una de les opcions indicades.")
def identificarmenu():
    if opcio[0] == "teclat":
        paraulesboges.text = input("Escriu la frase per teclat: ")
        paraulesboges.frasealeatoria = paraulesboges.fer_aleatories(paraulesboges.text)
        print(paraulesboges.frasealeatoria)
    elif opcio[0] == "link":
        print("link")
        #getDataFromApiNinja
    elif opcio[0] == "chatgpt":
        print("chatgpt")
        #getDataFromChatGPT()


menu()
identificarmenu()