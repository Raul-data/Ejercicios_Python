# Crea una lista de los números primos menores que un número dado por el usuario. Si el número dado es también primo deberá incluirlo también.

num_usuario = int(input("Dime un numero: "))

lista_numPrimos = []

for i in range(2, num_usuario + 1):
    es_primo = True
    
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            
    if es_primo:
        lista_numPrimos.append(i)
        
print(f"Numeros primos menores o el mismo numero si es primo, su numero {num_usuario}: {lista_numPrimos}")
