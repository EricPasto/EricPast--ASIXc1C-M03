def readInList():
    numbers = []
    try:
        punts = input(" ").split(" ")
        while not hem_acabat(punts):
            punts = input(" ").split(" ")
            numbers.append (int(punts))
            print(numbers)
    except:
        print("Error - Posa numeros!")
    return numbers
def hem_acabat(punts):
    acabat = False
    if punts[-1] == "-1":
        acabat = True
    return acabat