import crazy_words

def getDataFromKeyboard():
    crazy_words.Texto_Ordenado, crazy_words.frase = crazy_words.frase()
    crazy_words.palabras = crazy_words.separar()
    crazy_words.frase_Desordenado = crazy_words.juntar()
    crazy_words.resultado()