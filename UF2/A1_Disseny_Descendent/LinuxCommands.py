import random

llistacomandes = ['touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt']
llistaparametres = ['-h', '-help', '-v', '-version']
benvingudes = ["hola","benvingut","welcome"]
llegircomanda = []
print(random.choice(benvingudes))

def llegircomanda():
    llegircomanda = input('/home/Eric$ ').split(" ")
    if llegircomanda[0] not in llistacomandes:
        print(llegircomanda[0],"command not found")
    return llegircomanda

def identificarcomanda():
    if llegircomanda[0] == llistacomandes[0]:
        print("comanda 1")



llegircomanda()
identificarcomanda()
