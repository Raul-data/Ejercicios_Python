# Pide un texto largo. Crea un diccionario donde:
# Las claves sean cada palabra distinta y el valor el número de veces que aparece. 
# Los valores sean otro diccionario con: {"apariciones": x, "longitud": y}
# Muestra las 5 palabras más frecuentes.

texto = input("Introduce un texto largo: ")

palabras = texto

diccionario = {}

#Contamos palabras y guardamos datos
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra]["apariciones"] += 1
    else:
        diccionario[palabra] = {
            "apariciones" : 1,
            "longitud" : len(palabra)
        }
        
#Ordenamos por numero de apariciones
palabras_ordenadas = sorted
        
#Contamos las mas frecuentes
for i in range(5):
    palabra = palabras_ordenadas[i]
    
