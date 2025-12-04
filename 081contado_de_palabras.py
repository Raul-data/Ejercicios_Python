#Pide una frase al usuario y crea un diccionario donde las claves sean palabras y los valores el número de veces que aparece cada una.

frase_usuario = input("Dime una frase usuario: ")

palabras = frase_usuario.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
        
print(f"frecuencia de palabras {frecuencia}")
