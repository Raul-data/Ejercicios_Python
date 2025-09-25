# Dada una lista de números, elimina los números negativos y deja solo los positivos.

listanumeros = [1,-3,4,7,-7,-9]
listanueva = []
for i in listanumeros:
    if i < 0:
        listanueva.append(i)
print(listanueva)

# listanumeros = [1,-3,4,7,-7,-9]

# for i in listanumeros:
#      if i < 0:
#         listanumeros.remove(i)
#         print(listanumeros)