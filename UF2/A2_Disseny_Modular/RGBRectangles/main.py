import systemColors

#identificar la mesura del rectangle
#identificar el color amb el que pintar el rectangle
#crear el rectangle
#Com sortir

def identificarRectangle():
    dadesRectangle = []
    demanarRectangle = input(": ").split(" ")
    colorRectangle = demanarRectangle[0]
    yRectangle = demanarRectangle[-1]
    xRectangle = demanarRectangle[-2]
    dadesRectangle.append(demanarRectangle)
    while demanarRectangle[-1] != ";q":
        demanarRectangle = input(": ").split(" ")
        dadesRectangle.append(demanarRectangle)
    if colorRectangle == "Red":
        print (systemColors.CRED)
    print(dadesRectangle)

#def ferRectangle():
 #   pass

identificarRectangle()

