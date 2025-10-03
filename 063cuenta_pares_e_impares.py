# Dada una lista de números, cuenta cuántos son pares y cuántos son impares. Muestra los resultados por pantalla.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

Lista_pares = []
lista_impares = []

for i in numeros:
    if i % 2 == 0:
        Lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"Esta es la lista de pares: {Lista_pares} \nY esta es la de impares {lista_impares}")