"""
Eric Pastó
ASIX1B
19/4/2023
ParaulesBojes -R3
"""
import openai
openai.api_key ="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"
from UF2.A1_Disseny_Descendent.paraulesboges3 import paraulesboges3

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
        paraulesboges3.fer_aleatories()
    elif opcio[0] == "link":
        print("link")
        #getDataFromApiNinja
    elif opcio[0] == "chatgpt":
        print("chatgpt")
        #getDataFromChatGPT()


menu()
identificarmenu()