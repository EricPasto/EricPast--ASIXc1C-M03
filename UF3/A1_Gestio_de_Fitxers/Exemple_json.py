"""

En aquest exemple, primer definim el contingut JSON que volem escriure en un fitxer.
Després, utilitzem la funció json.dump() per escriure el contingut en un fitxer anomenat exemple.json.
A continuació, utilitzem la funció json.load() per llegir el contingut JSON del fitxer exemple.json i assignar-lo a la variable x.
Finalment, imprimim el contingut JSON amb la funció json.dumps() i utilitzem l'argument indent
per especificar la quantitat d'espais que volem utilitzar per a l'indentació del contingut.

"""

import json

# definim el contingut JSON

x = {
   "name": "John",
   "age": 30,
   "married": True,
   "divorced": False,
   "children": ("Ann", "Billy"),
   "pets": None,
   "cars": [
       {"model": "BMW 230", "mpg": 27.5},
       {"model": "Ford Edge", "mpg": 24.1}
   ]
}

# escriure el contingut JSON en un fitxer

with open('exemple.json', 'w') as f:
   json.dump(x, f)



# llegir el contingut JSON d'un fitxer

with open('exemple.json', 'r') as f:
   x = json.load(f)



# imprimir el contingut JSON

print(json.dumps(x, indent=4))