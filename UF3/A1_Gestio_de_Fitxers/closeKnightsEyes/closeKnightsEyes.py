with open("Knight.in", "r") as f:
    contenido = f.read()


contenido_modificado = contenido.replace('0', 'X')


with open("KnightEyesClosed.out", "w") as f:
    f.write(contenido_modificado)


print("Se ha creado el archivo Dragon_out.txt con los 0 reemplazados por X.")