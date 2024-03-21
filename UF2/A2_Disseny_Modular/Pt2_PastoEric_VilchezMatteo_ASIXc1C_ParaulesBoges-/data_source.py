import crazy_words
import requests
def getDataFromKeyboard():
    crazy_words.Texto_Ordenado, crazy_words.introduirfrase = crazy_words.introduirfrase()
    crazy_words.palabras = crazy_words.separar()
    crazy_words.frase_Desordenado = crazy_words.juntar()
    crazy_words.resultado()

def getDataFromChatGPT():
    crazy_words.Texto_Ordenado, crazy_words.obtener_respuesta = crazy_words.obtener_respuesta()
    crazy_words.palabras = crazy_words.separar()
    crazy_words.frase_Desordenado = crazy_words.juntar()
    crazy_words.resultado()

def getDataFromServer():
    name = 'Venus'
    api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'BR6T9qXRmBZVo5G6WSWBng==yoQ4qXectmeIun3M'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        crazy_words.Texto_Ordenado, crazy_words.introduirfrase = crazy_words.introduirfrase()
        crazy_words.palabras = crazy_words.separar()
        crazy_words.frase_Desordenado = crazy_words.juntar()
        crazy_words.resultado()

    else:
        print("Error:", response.status_code, response.text)

