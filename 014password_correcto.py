contrasena_correcta = "python123"
intento = " "

while intento != contrasena_correcta:
    intento = input("Dame la contraseña correcta: ")
    if intento == contrasena_correcta:
        print("Contraseña correcta bienvenido")
    else:
        print("Contraseña incorrecta, intentalo de nuevo")