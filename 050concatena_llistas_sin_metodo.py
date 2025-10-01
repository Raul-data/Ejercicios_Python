lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_nueva = []

cont = 0

for i in lista1:
    
    lista_nueva.append(lista1[cont])
    lista_nueva.append(lista2[cont])
    
    cont += 1
    
print(lista_nueva) 
    
