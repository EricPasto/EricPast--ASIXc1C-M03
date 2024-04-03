import crazy_words
import openai
openai.api_key = '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'
def getDataFromKeyboard():
    crazy_words.Texto_Ordenado, crazy_words.frase = crazy_words.frase()
    crazy_words.palabras = crazy_words.separar()
    crazy_words.frase_Desordenado = crazy_words.juntar()
    crazy_words.resultado()

def getDataFromChatGPT():
    from crazy_wordsGPT import resultado
    resultado()

def getDataFromServer():
    from crazy_wordsURL import resultado
    resultado()