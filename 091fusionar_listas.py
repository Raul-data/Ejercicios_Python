# Dadas dos listas: una con nombres y otra con teléfonos, crea un diccionario donde cada nombre sea clave y su teléfono el valor. Asume que ambas listas tienen la misma longitud.

nombres = ["Juan", "Ana", "Pedro", "Lucia"]

telefonos = ["66233234", "6232344", "6778234", "64233234"]

agenda = {}

for i in range(len(nombres)):
    agenda[nombres[i]] = telefonos[i]
    
print(agenda)