# Elimina los elementos duplicados de una lista sin usar funciones predeterminadas, finalmente imprime la nueva lista.

miLista = [1, 2, 2, 3, 4, 4, 1, 5]
listaSinDuplicados = []

for num in miLista:
    if num not in listaSinDuplicados:
        listaSinDuplicados.append(num)
        
print(f"Esta es la lista original -> {miLista} y esta seria la que no tiene duplicados -> {listaSinDuplicados}")