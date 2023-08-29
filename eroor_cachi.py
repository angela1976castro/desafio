import random

def jugar_cachipun():
    """Esta función nos permite jugar a cachipún"""
    print("¡Juguemos a cachipún!")
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        try:
            jugador = input("Elige una opción (piedra, papel o tijera): ").lower()

            if jugador not in opciones:
                raise ValueError("Opción inválida. Por favor, elige entre piedra, papel o tijera.")

            break  # Salimos del bucle si la opción es válida

        except ValueError as e:
            print(e)

    oponente = random.choice(opciones)

    print(f"Tú elegiste: {jugador}")
    print(f"El oponente eligió: {oponente}")

    if jugador == oponente:
        print("¡Es un empate!")
    elif ((jugador == "piedra" and oponente == "tijera") or (jugador == "papel" and oponente == "piedra")
            or (jugador == "tijera" and oponente == "papel")):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")


if __name__ == "__main__":
    jugar_cachipun()
