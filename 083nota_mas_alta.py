# Guarda en un diccionario 5 alumnos con su nota. Muestra el alumno con la nota más alta.

alumnos = {
    "euralia" : 6,
    "eufasio" : 2,
    "frisea" : 1,
    "eugilio" : 9,
    "perfasio" : 4
}

mejor_alumno = ""
mejor_nota = -1

for alumno in alumnos: 
    nota = alumnos[alumno]
    
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_alumno = alumno

print(f"El alumno con la nota mas alta es: {mejor_alumno} con la nota {mejor_nota}")