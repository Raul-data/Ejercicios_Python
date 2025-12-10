# Pide un texto al usuario y usa un diccionario para contar cuántas veces aparece cada letra (ignora espacios).

texto = input("Introduce un texto: ")

conteo = {}

for letra in texto:
    if letra != " ":
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

print(conteo)