# Define un diccionario donde cada clave es un país y el valor es una lista de ciudades que están en dicho país. Debe tener los países y ciudades de: España, Francia, Italia, Alemania y Estados Unidos. 
# Se le solicita al usuario que diga un país o una ciudad del mundo, el programa responderá con las ciudades que conoce de dicho país o a qué país corresponde la ciudad dada por el usuario.
# Si el usuario escribe España, mostrará su lista de ciudades.
# Si el usuario escribe Madrid, dirá que pertenece a España.
# Si no lo encuentra, muestra un mensaje de aviso.

paises = {
    "España": ["Madrid", "Barcelona", "Valencia"],
    "Francia": ["Paris", "Lyon", "Marsella"],
    "Italia": ["Roma", "Milan", "Venecia"],
    "Alemania": ["Berlin", "Munich", "Hamburgo"],
    "Estados Unidos": ["Nueva York", "Los Angeles", "Chicago"]
}

entrada = input("Introduce un pais o una ciudad: ")

encontrado = False

#primero comprobamos si es un pais 
if entrada in paises:
    print(f"Ciudades de {entrada}: {paises[entrada]}")
    encontrado = True
else:
    #si no es un pais buscamos si es una ciudad
    for pais in paises:
        if entrada in paises[pais]:
            print(f"{entrada} pertenece a {pais}")
            encontrado = True
            
# y si no encontramos nada se lo decimos al usuaro
if not encontrado:
    print("No se ha encontrado el pais ni la ciudad")