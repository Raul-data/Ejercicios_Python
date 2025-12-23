# Crea un diccionario vacío para añadir los datos de los alumnos de clase. El id será la clave, y debe ser incremental, es decir, a medida que se inserten nuevos usuarios aumentará en una unidad. 

# El valor de cada alumno será otro diccionario en el que guardará: nombre, edad y curso.

# Deberá implementar un menú con las siguientes opciones para trabajar sobre la "base de datos" creada con diccionarios: 
# añadir alumno
# borras alumno por id
# buscar alumnos por edad
# mostrar toda la tabla
# actualizar cada uno de los datos

seguir = True

# ID -> [nombre, edad, curso]
alumnos = {}
siguiente_id = 0

def limpiar_pantalla():
    for _ in range(5):
        print()
        
def añadir_alumno():
    nonlocal_id = obtener_siguiente_id()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    curso = input("Curso: ")
    alumnos[nonlocal_id] = [nombre, edad, curso]
    
    
def obtener_siguiente_id():
    global siguiente_id
    id_actual = siguiente_id
    siguiente_id += 1
    return id_actual


def borrar_por_id():
    id_borrar = int(input("Introduce un ID para borrar: "))
    if id_borrar in alumnos:
        del alumnos[id_borrar]
        print("Alumno borrado")
    else:
        print("ID no encontrado")
        
def buscar_por_edad():
    edad_buscar = int(input("Introduce edad a buscar: "))
    encontrado = False
    for id_alumno in alumnos:
        if alumnos[id_alumno][1] == edad_buscar:
            print(f"{id_alumno} : {alumnos[id_alumno][0]}, {alumnos[id_alumno][1]}, {alumnos[id_alumno][2]}")
            encontrado = True
    if not encontrado:
        print("No hay alumnos con esa edad.")
        
def mostrar_tabla():
    if not alumnos:
        print("No hay alumnos.")
    for id_alumno in alumnos:
        print(f"{id_alumno} : {alumnos[id_alumno][0]}, {alumnos[id_alumno][1]}, {alumnos[id_alumno][2]}")


def modificar_alumno():
    id_mod = int(input("Introduce ID a modificar: "))
    if id_mod in alumnos:
        nombre = input("Nuevo nombre: ")
        edad = int(input("Nueva edad: "))
        curso = input("Nuevo curso: ")
        alumnos[id_mod] = [nombre, edad, curso]
        print("Alumno modificado.")
    else:
        print("ID no encontrado.")


while seguir:
    print("\n0. Salir")
    print("1. Añadir alumno")
    print("2. Borrar alumno por ID")
    print("3. Buscar alumnos por edad")
    print("4. Mostrar todos los alumnos")
    print("5. Modificar alumno")

    opcion = int(input("Elige opcion: "))

    if opcion == 0:
        seguir = False
    elif opcion == 1:
        añadir_alumno()
    elif opcion == 2:
        borrar_por_id()
    elif opcion == 3:
        buscar_por_edad()
    elif opcion == 4:
        mostrar_tabla()
    elif opcion == 5:
        modificar_alumno()
    else:
        print("Opcion no valida.")