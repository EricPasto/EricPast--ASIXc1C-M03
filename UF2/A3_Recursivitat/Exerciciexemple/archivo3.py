
def Kconvertir_ASCII_03():
    texto = input("texto=")
    txtcodificar = []
    for algo in texto:
        if algo == " ":#esto es para que guarde las separacion 
            txtcodificar.append(" ")
        else:
            txtcodificar.append(str(ord(algo)))
            txtcodificar.append(".")
    if len(txtcodificar) > 0:
        txtcodificar = txtcodificar[:-1]# Eliminamos el último elemento de la lista
    for letra in txtcodificar:
        print(letra, end="")
    print("")
        

