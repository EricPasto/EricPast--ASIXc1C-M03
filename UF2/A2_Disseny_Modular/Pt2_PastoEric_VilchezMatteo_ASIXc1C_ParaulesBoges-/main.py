#import openai

#openai.api_key ="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"
import crazy_words

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
        crazy_words.Texto_Ordenado,frase = crazy_words.frase()
        crazy_words.palabras = crazy_words.separar()
        crazy_words.frase_Desordenado = crazy_words.juntar()
        crazy_words.resultado()
    elif opcio[0] == "link":
        print("link")
        #getDataFromApiNinja
    elif opcio[0] == "chatgpt":
        print("chatgpt")
        #getDataFromChatGPT()


menu()
identificarmenu()