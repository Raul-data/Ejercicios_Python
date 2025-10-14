# Si el usuario introduce el número 369 devolverá 3 centenas, 6 decenas, 9 unidades
numero = int(input("Dime un numero para descomponer por unidades: "))

centenas = numero // 100
numero = numero % 100
decenas = numero // 10
unidades = numero % 10

print(centenas, "centenas,", decenas, "decenas,", unidades, "unidades")
