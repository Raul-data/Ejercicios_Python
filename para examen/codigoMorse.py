# === EJERCICIO: TRADUCTOR A CÓDIGO MORSE SIN DICCIONARIOS ===
# Usamos listas paralelas: una para letras/números y otra para su código Morse

# Listas paralelas
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ', ',', '.', '?'
]

morse = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
    '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
    '..-', '...-', '.--', '-..-', '-.--', '--..',
    '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',
    '   ', '--..--', '.-.-.-', '..--..'
]

# Pedir texto al usuario
texto = input("Introduce el texto a traducir a Morse (solo letras, números, espacio, coma, punto y ?): ").upper()

# Variable para almacenar el resultado
resultado = []

# Recorrer cada carácter del texto
for char in texto:
    encontrado = False
    # Buscar el carácter en la lista de letras
    for i in range(len(letras)):
        if char == letras[i]:
            resultado.append(morse[i])
            encontrado = True
            break
    
    # Si no se encuentra el carácter, añadir un símbolo de error o ignorarlo
    if not encontrado:
        resultado.append('?')  # Carácter no soportado

# Unir los códigos Morse con espacios y mostrar el resultado
print("\nTexto en Morse:")
print(' '.join(resultado))