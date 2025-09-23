num_secreto = 7
num_usuario = int(input("Dime un numero para adivinarlo: "))
intentos = 0

while intentos <= 6 and num_usuario != num_secreto:
    num_usuario = int(input("Dime un numero para adivinarlo: "))
    intentos += 1
    
if intentos == 6:
    print("No lo has acertado")