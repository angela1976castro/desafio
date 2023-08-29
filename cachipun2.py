import random

def jugar_cachipun2():
    """ Función para jugar cachipun
    """

    opciones = ["piedra", "papel", "tijera"] #opciones para que el computador escoge

    jugador = input("Ingresa una opción (piedra, papel, tijera): ").lower() #se pide una opcion y se convierte a minuscula

    if jugador not in opciones: #si la eleccion del jugador no esta en la variable opciones se lanza el error
        print("Opcion incorrecta...")
        
    else: #si la elección esta dentro de la variable opciones se continua con el juego
        oponente = random.choice(opciones) #el computador escoge una opcion de la variable opciones
        print(f"El oponente escogio {oponente}") # se imprime la elección del computador
        
        #situaciones donde el jugador gana
        if (jugador == "piedra" and oponente == "tijera") or (jugador == "papel" and oponente == "piedra") or (jugador == "tijera" and oponente == "papel"):
            print("¡Ganaste!")
            
        #situaciones donde el jugador y el computador empatan
        elif jugador == oponente:
            print("¡Empate!")
        
        #situaciones donde el jugador pierde
        else:
            print("¡¡¡Perdiste!!!")
if __name__ =="__main__":
    jugar_cachipun2()