"""
    Matteo Vilchez.
    03/04/2024
    ASIXc 1C  M03 UF2 A1
    Repaso
"""
#Paràmetres Posicionals
#El paràmetre ha de coincidir en posició:

def sumar(n1,n2):

   return n1+n2



sumar(5,7)  # 12

sumar(4)    # TypeError: sumar() missing 1 required positional argument: 'n2'


#Valor per defecte
#A més podem tenir paràmetres amb valors per defecte:

def operar(n1, n2, operador='+', resposta='El resultat és '):

   resultat= resposta

   if operador=="+":

       resultat= resultat + str(n1+n2)

   elif operador=="-":

       resultat= resultat + str(n1-n2)

   else:

       resultat= resultat +  "BACALAOOOOOOO"

   return resultat



print(operar(5,7))                     #'El resultado es 12'

print(operar(5,7,"-"))                 #'El resultado es -2'

print(operar(5,7,"-","La resta es "))  #'La resta es -2'

print(operar(5,7,"/"))                 # El resultat és BACALAOOOOOOO


#Paràmetres keyword
#Són aquells on s'indiquen el nom del paràmetre i el seu valor, per tant no és necessari que tinguin la mateixa posició.

#En definir una funció o en cridar-la, cal indicar primer els arguments posicionals i a continuació els arguments amb valor per defecte (keyword).

print("Keyword")

print(operar(5,7))         # dos paràmetres posicionals

print(operar(n1=4,n2=6))   # dos parámetros keyword

print(operar(n2=6,n1=4))  # al fer servir el NOM es poden CANVIAR de LLOC



print(operar(4,6,resposta="La suma és: "))    		 # dos paràmetres posicionals i uno keyword

print(operar(4,6,resposta="La resta és: ",operador="-")) # dos paràmetres posicionals i dos keyword