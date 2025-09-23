# Preguntará al usuario qué color borrar de los que hay en la lista colores del ejercicio anterior.


colores = ["rojo", "verde", "azul", "amarillo"]

print(f"La lista sin elimnar {colores}")

elimninar = input("Que color quieres eliminar: ")

colores.remove(elimninar)

print(f"Esta es la lista con el color eliminado {colores}")