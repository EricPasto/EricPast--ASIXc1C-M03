"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""


def setLogin(nomUsuari, contraseña, intents):
    # Verificar si el nombre de usuario y la contraseña son correctos
    if nomUsuari == contraseña:
        return True, intents
    else:
        return False, intents - 1

def mostrarASCII():
    # Mostrar la foto ASCII
    print("Bienvenido al Sistema!")
    # Aquí puedes incluir la representación ASCII de la cara del usuario

def login():
    # Solicitar nombre de usuario, contraseña e intentos al usuario
    nomUsuari = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")
    intents = int(input("Introduce la cantidad de intentos: "))

    # Realizar el proceso de inicio de sesión
    while intents > 0:
        correcto, intents = setLogin(nomUsuari, contraseña, intents)
        if correcto:
            mostrarASCII()
            break
        else:
            if intents == 0:
                print("Error: se ha agotado el número de intentos!")
                break
            else:
                print("Error: Nombre de usuario o contraseña errónea!")
                nomUsuari = input("Introduce tu nombre de usuario: ")
                contraseña = input("Introduce tu contraseña: ")

# Iniciar el proceso de inicio de sesión
login()