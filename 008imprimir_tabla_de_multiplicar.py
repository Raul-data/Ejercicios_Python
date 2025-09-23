tabla = int(input("Que tabla de multiplicar quieres: "))
num = int(input("Hasta que numero quieres: "))

for i in range(1,num + 1 ):
    print(tabla, " x ", i, " = " , tabla * i)