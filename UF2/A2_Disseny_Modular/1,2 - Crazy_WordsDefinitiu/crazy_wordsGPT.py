import random
import requests

cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
palabras = []

def obtener_respuesta_chatgpt(prompt):
    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": "Bearer TU_CLAVE_DE_API",  # Reemplaza con tu clave de API de OpenAI
                "Content-Type": "application/json"
            },
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 50
            }
        )
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["text"].strip()
        else:
            print("Error - No se pudo obtener la respuesta de ChatGPT.")
            return None
    except Exception as e:
        print("Error -", e)
        return None

def separar(texto):
    palabras = texto.split()
    for i, palabra in enumerate(palabras):
        if len(palabra) >= 3:
            if palabra[-1] in cEspeciales and palabra[-2] not in cEspeciales:
                sep = list(palabra[1:-2])
                random.shuffle(sep)
                palabras[i] = palabra[0] + ''.join(sep) + palabra[-2] + palabra[-1]
            else:
                sep = list(palabra[1:-1])
                random.shuffle(sep)
                palabras[i] = palabra[0] + ''.join(sep) + palabra[-1]
    return ' '.join(palabras)

def resultado():
    prompt = input("Introduce el texto para ChatGPT: ")
    respuesta_chatgpt = obtener_respuesta_chatgpt(prompt)
    if respuesta_chatgpt:
        texto_desordenado = separar(respuesta_chatgpt)
        print("Texto desordenado:")
        print(texto_desordenado)

#resultado()