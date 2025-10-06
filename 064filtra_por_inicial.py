# Dada una lista de palabras, filtra aquellas que comienzan con una letra dada por el usuario. Utilizar el método startswith. 
# palabras = ["sol", "luna", "mar", "estrella", "cielo"]  

# método --> palabras.startswith(letra)

palabras = ["sol", "luna", "mar", "estrella", "cielo"] 
nuevas_palabras = []
letra_usuario = input("Dime una letra para darte las palabras que salen en la lista con esa letra: ")

for i in palabras:
    
    if i.startswith(letra_usuario):
        nuevas_palabras.append(i)
        
print(f"esta son las palabras de la lista {nuevas_palabras}, tu letra a sido {letra_usuario}")