factorial = int(input("Dime un numero para darte el factorial: "))
num1 = 1

for i in range(1,factorial + 1):
    num1 *= i

print(f"el factorial de {factorial} es: {num1}")