palabra = ["a","p","o","w","u"]
contador = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        contador += 1
        
print("Tiene ", contador , " vocales")