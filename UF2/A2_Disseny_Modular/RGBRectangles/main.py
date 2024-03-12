import systemColors

llista = []
rectangulos = []

colors = {
    "RED": systemColors.CRED,
    "BLUE": systemColors.CBLUE,
    "YELLOW": systemColors.CYELLOW,
    "BLACK": systemColors.CBLACK,
    "WHITE": systemColors.CWHITE,
    "VIOLET": systemColors.CVIOLET,
    "GREEN": systemColors.CGREEN
}
def forma(color, ancho, alto):
    try:
        rectangulo = ""
        for i in range(ancho):
            for l in range(alto):
                rectangulo += colors[color.upper()] + "x "
            rectangulo += "\n"
        rectangulos.append(rectangulo)
    except KeyError:
        print("El color que acabas de introducir no está en la lista")

# Solicitar rectángulos hasta que se ingrese ";q" o ";Q"
while True:
    rectangle = input("Introduce el rectángulo (color ancho largo): ")
    if rectangle.lower() in (';q', ';Q'):
        break
    paraules = rectangle.split()
    color = paraules[0]
    ancho = int(paraules[1])
    alto = int(paraules[2])
    forma(color, ancho, alto)

# Imprimir todos los rectángulos
for r in rectangulos:
    print(r)

