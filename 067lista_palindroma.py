# Verificas si una lista es palíndroma, es decir, de elementos se lee igual de izquierda a derecha que de derecha a izquierda.
lista = [1, 2, 3, 2, 1]
palindroma = False

if lista == lista[::-1]:
    palindroma = True
    
if palindroma:
    print("La lista es palindroma.")
else:
    print("La lista no es palindroma.")