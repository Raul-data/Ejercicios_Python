numero = int(input("Cual es el numero maximo que quieres: "))
cuenta = 0

for i in range(1,numero + 1):
    cuenta = i + cuenta
    
print(cuenta)