palabra = input("Dime una palabra: ")
contador = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        contador += 1
        
print("Tiene ", contador , " vocales")