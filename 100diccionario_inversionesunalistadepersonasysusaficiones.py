# aficiones = {
#     "Guillermo": ["cine", "fútbol", "música"],
#     "Sebas": ["ajedrez", "cine"],
#     "Misael": ["música", "lectura"],
#     (añadir más gente)
# }
# Crea un diccionario inverso donde:
# clave = afición y valor = lista de personas que la practican.

# Finalmente mostrará un listado en el que aparezca afición y aficionados.

aficiones = {
    "Guillermo": ["cine", "fútbol", "música"],
    "Sebas": ["ajedrez", "cine"],
    "Misael": ["música", "lectura"],
    "Andrea": ["cine", "lectura"],
    "Carlos": ["fútbol"]
}

aficiones_inverso = {}
for persona in aficiones:
    for aficion in aficiones[persona]:
        if aficion not in aficiones_inverso:
            aficiones_inverso[aficion] = [persona]
        else:
            aficiones_inverso[aficion].append(persona)
            
for aficion in aficiones_inverso:
    print(f"{aficion}: {aficiones_inverso[aficion]}")