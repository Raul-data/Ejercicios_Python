# Crea una lista de varias palabras y elimina aquellas que tengan menos de 4 caracteres.

lista = ["hola", "tu", "cocodrilo", "mono", "por", "si"]
palabras = []

for i in lista:
    if len(i) >= 4:
        palabras += [i]
print(f"La lista de palabras es: {lista} y estas son las plabras que se quedan {palabras}") 

