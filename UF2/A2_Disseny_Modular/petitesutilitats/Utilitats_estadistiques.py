import paraulesboges

def calcular_mediana(a, b):
    return (a + b) / 2
def calculo_mediana():
    numeros = input("Ingresa dos números separados por un espacio: ")
    a, b = map(int, numeros.split())
    mediana = calcular_mediana(a, b)
    print("La mediana de", a, "y", b, "es:", mediana)
def calculo_mitjana():
    print("Càlcul de la mitjana...")
def calculo_desviestandard():
    print("Càlcul de la desviació estandard...")
