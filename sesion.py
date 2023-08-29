def iniciar_sesion():
    # Credenciales predefinidas (reemplaza estos valores con los que desees)
    usuario_valido = "usuario"
    contrasena_valida = "contraseña"

    # Solicitar al usuario que ingrese su nombre de usuario y contraseña
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")

    # Verificar las credenciales ingresadas
    if usuario_ingresado == usuario_valido and contrasena_ingresada == contrasena_valida:
        print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario_ingresado))
    else:
        print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    iniciar_sesion()
