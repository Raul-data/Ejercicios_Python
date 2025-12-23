# Pide nombres de candidatos para ser delegado de clase y crea un diccionario con sus votos iniciales a 0.

# Después, pide votos a los compañeros de clase (nombre del candidato) hasta que el usuario escriba “fin”.

# Incrementa los votos en el diccionario.

# Muestra el listado de los candidatos con el número de votos y el ganador.

candidatos = {
    "Juan": 0,
    "Paulino": 0,
    "Euralia": 0,
    "Estefeo": 0,
    "Pifasio": 0
}

voto = ""

while voto != "fin":
    voto = input("Vota a un candidato o pon fin: ")
    
    if voto != "fin" and voto in candidatos:
        candidatos[voto] += 1
        
print(candidatos)