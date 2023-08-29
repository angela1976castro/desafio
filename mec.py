import math

# Definimos el módulo para el cálculo de la velocidad en función del tiempo y distancia
def calcular_velocidad(tiempo, distancia):
    velocidad = distancia / tiempo
    return velocidad

# Función para obtener la entrada de datos del estudiante
def obtener_datos_estudiante():
    tiempo = float(input("Ingresa el tiempo de medición en segundos: "))
    distancia = float(input("Ingresa la distancia medida en metros: "))
    return tiempo, distancia

# Definimos la función principal para ejecutar el programa
def main():
    while True:
        try:
            print("\n--- Cálculo de velocidad ---")
            tiempo_medicion, distancia_medicion = obtener_datos_estudiante()

            # Calcular velocidad en función del tiempo y distancia proporcionados
            velocidad_calculada = calcular_velocidad(tiempo_medicion, distancia_medicion)

            # Imprimir resultado
            print(f"La velocidad medida es de {velocidad_calculada:.2f} m/s.")

        except ValueError:
            print("Error: Los datos ingresados no son válidos.")
        except ZeroDivisionError:
            print("Error: La distancia no puede ser cero. Revisa los datos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

        opcion = input("¿Deseas realizar otro cálculo? (s/n): ")
        if opcion.lower() != 's':
            break

if __name__ == "__main__":
    main()
