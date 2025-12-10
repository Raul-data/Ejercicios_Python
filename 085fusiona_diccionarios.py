# Dados dos diccionarios con valores numéricos, crea un tercero que tenga la suma de los valores de ambas claves (si la clave solo está en uno, se copia tal cual).

dic1 = {"a": 1, "b": 3, "c": 5}
dic2 = {"b": 2, "c": 4, "d": 6}

resultado = {}

for clave in dic1:
    resultado[clave] = dic1[clave]
    
for clave in dic2:
    if clave in resultado:
        resultado[clave] += dic2[clave]
    else:
        resultado[clave] = dic2[clave]
        
print(resultado)
        