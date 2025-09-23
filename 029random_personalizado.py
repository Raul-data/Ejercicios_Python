import random

num_inferior = int(input("Dime un numero inferior: "))
num_superior = int(input("Dime un numero superior: "))
num_cantidad = int(input("Dime la cuantos numeros random quieres: "))

for i in range(num_cantidad):
    num_cantidad += i
    num_aleatorio = random.randint(num_inferior,num_superior)

    print(f"El numero aleatorio entre {num_inferior} y {num_superior} es: {num_aleatorio}")
