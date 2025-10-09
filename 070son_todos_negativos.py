# Verifica si todos los números de una lista son negativos e imprímelos.cuantos numeros negativos hay de negativos

lista = [-5, -3, -1, 0, 2, 4, 6]
contador = 0
for i in lista:
    if i < 0:
        print(f"negativos son estos: {i}")
        contador += 1
print(f"Hay {contador} negativos")
