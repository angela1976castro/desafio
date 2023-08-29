from login import *
from cachipun2 import *



def main():
    print("Bienvenido a la aplicación de inicio de sesión para juegos")

    # Llamamos al módulo de inicio de sesión
    if login():
        jugar_cachipun2()  # Agregamos la opción de jugar a cachipún después de iniciar sesión
    else:
        print("Vuelve a ingresar")

# Llamamos al módulo principal
if __name__ == "__main__":
    main()
