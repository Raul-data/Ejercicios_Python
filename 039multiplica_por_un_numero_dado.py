# multiplica todos los elementos de la lista por un número dado por el usuario

lista = [2, 4, 5, 6, 8]
num_usuario = int(input("Dame un numero para multiplicar con la lista: "))

for i in range(len(lista)):

    lista[i] = num_usuario * lista[i]

print(lista)
