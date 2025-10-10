# Pide al usuario un número de 1 a 3 dígitos. Si el usuario da el número 120  mostrará 120 = 2x2x2x3x5

numero_usuario = int(input("dame un numero de 1 a 3 digitos: "))

original = numero_usuario
factores = []
divisor = 2

while numero_usuario > 1:
    if numero_usuario % divisor == 0:
        factores += [divisor]
        numero_usuario = numero_usuario // divisor
    else:
        divisor += 1
        
# Convierte factores a string y los une con "x" entre ellos
print(original, "=", "x".join(str(x) for x in factores))
