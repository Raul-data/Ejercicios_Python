# Dada una frase por el usuario, contad cuántas palabras tiene;
# utilizar split()

# palabras = cadena.split()
frase = input("Dime una frase para contar las palabras: ")

for i in frase:
    palabras = frase.split()
    
print(palabras)