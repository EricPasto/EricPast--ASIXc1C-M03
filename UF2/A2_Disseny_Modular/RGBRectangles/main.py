import systemColors

#identificar la mesura del rectangle
#identificar el color amb el que pintar el rectangle
#crear el rectangle
#Com sortir

colors={
    "RED": systemColors.CRED,
    "BLUE": systemColors.CBLUE,
    "YELLOW": systemColors.CYELLOW,
    "BLACK": systemColors.CBLACK,
    "WHITE": systemColors.CWHITE,
    "VIOLET": systemColors.CVIOLET,
    "GREEN": systemColors.CGREEN
}
#def identificarRectangle():
def ferRectangle():
    pass
    try:
        for i in range(xRectangle):
            for l in range(yRectangle):
                print(colors[paraules[0].upper()]+ "x ", end="")
            print("")
    except:
        print("El color que acabas de introducir no esta en la lista")


dadesRectangle = []
finish = False
demanarRectangle = input(": ")
paraules = demanarRectangle.split()
yRectangle = int(paraules[1])
xRectangle = int(paraules[2])
dadesRectangle.append(demanarRectangle)
while not finish:
    demanarRectangle = input(": ").split(" ")
    dadesRectangle.append(demanarRectangle)
    ferRectangle()
    if demanarRectangle[0] == ';q' or demanarRectangle[0] == ';Q':
        finish = True

    #return paraules, yRectangle, xRectangle


#identificarRectangle()
