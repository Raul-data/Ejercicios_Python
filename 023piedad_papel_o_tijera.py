jug1 = input("Jugador 1 (piedra 🗿, papel 🧻, tijeras ✂️): ").lower() 
jug2 = input("Jugador 2 (piedra 🗿, papel 🧻, tijeras ✂️): ").lower()

match (jug1, jug2):
    case (x, y) if x == y:
        print("Empate")
    case ("piedra", "tijeras") | ("tijeras", "papel") | ("papel", "piedra"):
        print("Jugador 1 gana")
    case ("tijeras", "piedra") | ("papel", "tijeras") | ("piedra", "papel"):
        print("Jugador 2 gana")
    case _:
        print("Jugada no válida")