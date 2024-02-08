
#lo que he echo es que un contador el cual cundo se escriba dentro lo guradara ya de que asi cundo entre en el for algo in contador 
#Ara que mi otra variable que es var comienze hacer un mas en cada vuelta asi cuando le des printar te printe el numero de letras  

def kcontar_letras_01():
    palabra = input("texto=")
    contador = 0
    for algo in palabra:
        if algo == " ":#aqui lo que he echo es que cundo algo que serai la vuelta es igual a un espacio reste en la variable var 
            contador = contador - 1
        contador = contador + 1
    print(contador)


