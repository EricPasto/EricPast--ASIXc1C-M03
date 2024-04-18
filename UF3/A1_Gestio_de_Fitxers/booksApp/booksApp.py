#NO ACABAT!


nomLlibres = []
nomAutors = []
numPagines = []

numLlibres = int(input("Numero de llibres: "))

try:
    file = open("books.out", mode ="w", encoding="utf-8")
    for l in range (numLlibres):
        in_nomLlibres = input("Nom: ")
        nomLlibres.append(in_nomLlibres)
        in_nomAutors = input("Autor/a: ")
        nomAutors.append(in_nomAutors)
        in_numPagines = int(input("Pagines: "))
        numPagines.append(in_numPagines)
        file.write(in_nomLlibres, in_nomAutors,  in_numPagines)
        file.close()
except:
    print("Error - Posa valors valids")




print("Se ha creado el archivo con los datos de los libros.")