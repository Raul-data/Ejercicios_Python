# adivina el numero random el usuario tiene 6 intentos para adivinar el numero random creado

import random

numero_randon = random.randint(1, 6)
intentos = 0

while intentos < 6:
    numero = int(input("dime el numero que estoy pensando entre el 1 y 6: "))
    intentos += 1
    if numero == numero_randon:
        print(f"Acertaste el numero es {numero_randon}")
        break
    else:
        print(f"Ese no es el numero, te queda {6 - intentos} intentos")

if numero != numero_randon:
    print(f"Perdiste, el numero era {numero_randon}")