from datetime import date
from datetime import datetime
from time import sleep

def obteOpcio():
    print("opció 1")
    print("opció 2")
    print("opció 3")
    print("opció 4")
    print("sortir 5")
    return int(input(""))
def opcio1():
    print("opcio 1 seleccionada")
    sleep(1)
def opcio2():
    print("opcio 2 seleccionada")
    sleep(1)
def opcio3():
    print("opcio 3 seleccionada")
    sleep(1)
def opcio4():
    print("opcio 4 seleccionada")
    sleep(1)
def tractarerror(missatge):
    avui = date.today()
    ara = datetime.now()
    avui= avui.strftime("%B %d, %Y")
    ara = ara.strftime("")
    print(f"{avui}\n{ara}\nERROR:{missatge}")

opcio = obteOpcio()
while opcio != 5:
    if opcio < 1 or opcio > 4:
        tractarerror("opcio no valida")
        opcio=int(input("Torna a indicar l'opció: "))
    else:
        if opcio == 1:
            opcio1()
        elif opcio == 2:
            opcio2()
        elif opcio == 3:
            opcio3()
        elif opcio == 4:
            opcio4()
        break

