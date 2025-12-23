# Tienes una lista de palabras y posteriormente crea un diccionario donde las claves sean las letras iniciales y los valores listas con todas las palabras que empiezan por esa letra, ordenadas alfabéticamente de forma ascendente.


palabras = ["casa", "coche", "avion", "barco", "bicicleta", "camion", "abeja"]

diccionario = {}

for palabra in palabras:
    letra = palabra[0]
    
    if letra not in diccionario:
        diccionario[letra] = []
        
    diccionario[letra].append(palabra)
    

for letra in diccionario:
    diccionario[letra].sort()

print(diccionario)