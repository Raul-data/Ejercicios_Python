num1 = int(input("Dame un numero"))
num2 = ""

while num1 != 0 and num2 != 0:
    num2 = int(input("Dame un numero"))
    num1 += num2 

print("La suma del total es: ", num1)