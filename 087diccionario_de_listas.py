# Crea un diccionario donde las claves sean asignaturas y los valores una lista de tres notas. Calcula la media de cada asignatura y muéstrala.

notas = {
    "Matématicas": [5,7,9],
    "Lengua": [7,8,8],
    "Historia": [6,9,6]
}

for asignatura in notas:
    media = sum(notas[asignatura]) / len(notas[asignatura])
    print(f"de {asignatura} la media es {media}")
