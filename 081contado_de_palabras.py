#Pide una frase al usuario y crea un diccionario donde las claves sean palabras y los valores el número de veces que aparece cada una.

frase = input("Introduce una frase: ")

frecuencia = {}

palabra = ""

for char in frase:
    if char != " ":
        palabra += char
    else:
        if palabra != "":
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        palabra = ""
        
if palabra != "":
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
        
print(frecuencia)