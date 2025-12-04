postales = {
    "Madrid": 28001,
    "Barcelona": 18001,
    "Valencia": 46001
}

print(f"sin invertir: {postales}")

#invertido
invertido ={valor: clave for clave, valor in postales.items()}

print(f"Invertido: {invertido}")