n = int(input("De cuanto quieres el triangulo: "))

for i in range(n + 1):
    j = 1
    while j <= n - i:
        print(" ", end= " ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end= " ")
        j += 1
    print()
    
