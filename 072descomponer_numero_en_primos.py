#Pide al usuario un número de 1 a 3 dígitos. Si el usuario da el número 120  mostrará 120 = 2x2x2x3x5

numero_usuario = int(input("Dime un numero de 1 a 3 digitos: "))
original = numero_usuario
factores = []
primo = 2

while primo * primo <= numero_usuario:
    while numero_usuario % primo == 0:
        factores += [primo]
        numero_usuario = numero_usuario // primo
    primo += 1
if numero_usuario > 1:
    factores += [numero_usuario]
print(f"{original} = {primo}")