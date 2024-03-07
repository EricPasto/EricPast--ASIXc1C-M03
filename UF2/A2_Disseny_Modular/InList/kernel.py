def readInList():
    numbers = []
    #try:
    punts = input(" ").split(" ")
    while not hem_acabat(punts):
        numbers.append(punts)
        punts=input(" ").split(" ")
        print(numbers)
    #except:
        #print("Error - Posa numeros!")
    return numbers
def hem_acabat(punts):
    acabat = False
    if punts[-1] == "-1":
        acabat = True
    return acabat