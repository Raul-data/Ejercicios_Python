# Comprobar que un número dado por el usuario es primo o no lo es. Un número primo es aquel cuyos únicos divisores son el 1 y el mismo número.

numero = int(input("Introduce un numero: "))

if numero <= 1:
    print(f"{numero} no es un numero primo")
else:
    es_primo = True
    for i in range(2,numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print(f"{numero} Es primo")
else:
    print(f"{numero} No es primo")

