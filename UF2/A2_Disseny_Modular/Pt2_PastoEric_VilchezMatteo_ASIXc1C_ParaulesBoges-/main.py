#import openai

#openai.api_key ="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"
import crazy_words
import data_source
opcio = []
def menu():
    demanar = input("Chatgpt(C), Teclat(T), Link(L): ")
    if demanar == 'T' or demanar == 't':
        opcio.append("teclat")
    elif demanar == "L" or demanar == 'l':
        opcio.append("link")
    elif demanar == "C" or demanar == 'c':
        opcio.append("chatgpt")
    else:
        print("Error, indica una de les opcions indicades.")
def identificarmenu():
    if opcio[0] == "teclat":
        data_source.getDataFromKeyboard()
    elif opcio[0] == "link":
        print("link")
        #getDataFromApiNinja
    elif opcio[0] == "chatgpt":
        print("chatgpt")
        #getDataFromChatGPT()


menu()
identificarmenu()