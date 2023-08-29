import random
# Módulo de juego de cachipún


def jugar_cachipun():
    """Esta función nos permite jugar a cachipun"""
    print("¡Juguemos a cachipún!")
    opciones = ["piedra", "papel", "tijera"]
   # Solicitar al jugador que elija una opción
   
    jugador = input("Elige una opción (piedra, papel o tijera): ").lower()



    # Validar la opción del jugador
    if jugador not in opciones:
        print("Opción inválida. Por favor, elige entre piedra, papel o tijera.")
        return

   # Generar la opción del oponente de forma aleatoria
    
    oponente = random.choice(opciones)

    print(f"Tú elegiste: {jugador}")
    print(f"El oponente eligió: {oponente}")

    # Determinar el resultado del juego
    if jugador == oponente:
        print("¡Es un empate!")
    elif ((jugador == "piedra" and oponente == "tijera") or (jugador == "papel" and oponente == "piedra")
           or (jugador == "tijera" and oponente == "papel")):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")


# usando el bloque if __name__ solo para este archivo
if __name__ == "__main__":
    jugar_cachipun()
