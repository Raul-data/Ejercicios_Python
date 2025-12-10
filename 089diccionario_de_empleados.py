# Crea un diccionario donde la clave sea el DNI y el valor otro diccionario con nombre, puesto, sueldo. Muestra todos los nombres de los empleados.

empleados = {
    "1111111A":{
        "nombre" : "Juan",
        "puesto" : "programador",
        "sueldo" : 2000
    },
    "22222222B" :{
        "nombre" : "Ana",
        "puesto" : "diseñedaora",
        "sueldo" : 2100
    },
    "333333C" :{
        "nombre" : "Pedro",
        "puesto" : "analista",
        "sueldo" : 1900
    },
    "4444V" :{
        "nombre" : "Marta",
        "puesto" : "tester",
        "sueldo" : 2200
    }
}

for dni in empleados:
    print(empleados[dni]["nombre"])