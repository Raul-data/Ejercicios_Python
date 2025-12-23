# Pide un texto largo. Crea un diccionario donde:
# Las claves sean cada palabra distinta y el valor el número de veces que aparece. 
# Los valores sean otro diccionario con: {"apariciones": x, "longitud": y}
# Muestra las 5 palabras más frecuentes.

texto = input("Introduce un texto: ")

palabras = texto.split()
diccionario = {}

#Contamos las palabras y guardamos la longitud
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra]["apariciones"] += 1
    else:
        diccionario[palabra] ={
            "apariciones" : 1,
            "longitud" : len(palabra)
        }
        
        
#Mostramos las 5 palabras mas frecuentes 
for _ in range(5):
    max_palabra = ""
    max_apariciones = 0
    
    for palabra in diccionario:
        if diccionario[palabra]["apariciones"] > max_apariciones:
            max_apariciones = diccionario[palabra]["apariciones"]
            max_palabra = palabra
            
    if max_palabra != "":
        print(max_palabra, diccionario[max_palabra])
        diccionario[max_palabra]["apariciones"] = 0

