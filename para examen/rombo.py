n = 5

# Parte superior (incluye la fila central)
i = 0
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# Parte inferior (sin repetir la fila central)
i = n - 1
while i >= 0:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end=" ")
        j += 1
    print()
    i -= 1