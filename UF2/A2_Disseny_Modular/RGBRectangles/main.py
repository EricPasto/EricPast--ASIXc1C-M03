import systemColors

llista = []
rectangulos = []

colores = {
    "RED": systemColors.CRED,
    "BLUE": systemColors.CBLUE,
    "YELLOW": systemColors.CYELLOW,
    "BLACK": systemColors.CBLACK,
    "WHITE": systemColors.CWHITE,
    "VIOLET": systemColors.CVIOLET,
    "GREEN": systemColors.CGREEN
}
def crearforma(color, ancho, alto):
    try:
        rectangulo = ""
        for i in range(ancho):
            for l in range(alto):
                rectangulo += colores[color.upper()] + "x "
            rectangulo += "\n"
        rectangulos.append(rectangulo)
    except KeyError:
        print("El color que acabas de introducir no está en la lista")

# Solicitar rectángulos hasta que se ingrese ";q" o ";Q"
while True:
    pedirRectangulo = input("Introduce el rectángulo (color ancho largo): ")
    if pedirRectangulo.lower() in (';q', ';Q'):
        break
    paraules = pedirRectangulo.split()
    color = paraules[0]
    ancho = int(paraules[1])
    alto = int(paraules[2])
    crearforma(color, ancho, alto)

# Imprimir todos los rectángulos
for r in rectangulos:
    print(r)

