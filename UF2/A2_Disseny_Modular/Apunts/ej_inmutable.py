"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""
#Objecte immutable
#Evidentment, si es passa un valor d'un objecte immutable, el seu valor no es podrà canviar dins de la funció:

def unaFuncio(a):

   a=999999



a=0

unaFuncio(a)

print(a)       # 0



#Objecte mutable
#No obstant això, si passem un objecte d'un tipus mutable, si podrem canviar el seu valor:

def unaAltraFuncio(llista):

   llista.append(3)

   llista.append(4)

   llista.append(5)



unaLlista = [1,2]

unaAltraFuncio(unaLlista)

print(unaLlista)    # [1, 2, 3, 4, 5]