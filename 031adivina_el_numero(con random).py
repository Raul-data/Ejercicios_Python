import random

num_usuario = int(input("Adivina el numero entre el 1 y el 10: "))
contador = 0

while contador <= 4:
    num_aleatorio = random.randint(1, 10)
    contador += 1

    if num_usuario == num_aleatorio:
        print(
            f"Felicidades, has adivinado el numero {num_aleatorio} en el intento {contador}"
        )
        break
    elif contador == 4:
        print(f"Lo siento has agotado tus intentos, el numero era {num_aleatorio}")
        break
    else:
        print(f"Lo siento intentalo de nuevo")
        num_usuario = int(input("Adivina el numero entre el 1 y el 10: "))
