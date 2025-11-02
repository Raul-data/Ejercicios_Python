num1 = int(input("Dime un numero para hacer el fibonacci:"))
a = 0
b = 1

for i in range(num1):
    c = a 
    a = b
    b = c + a
    print(a, end=" ")