n = int(input("De cuanto quieres el triangulo: "))
simbolo = input("que simbolo quieres")


for i in range(0,n + 1):
    for j in range(i):
        print(simbolo, end=" ")
    print()