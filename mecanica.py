# Importamos los módulos necesarios

import random
import time

# Definimos una función para simular los datos del sensor de velocidad
def obtener_datos_sensor():
    # En este caso, simulamos la obtención de datos de velocidad entre 30 y 100 km/h
    return random.randint(30, 100)

# Definimos el módulo para el cálculo de la velocidad en función del tiempo y distancia
def calcular_velocidad(tiempo, distancia):
    velocidad = distancia / tiempo
    return velocidad

# Definimos el módulo para obtener el valor absoluto de la velocidad
def velocidad_absoluta(velocidad):
    return abs(velocidad)

# Definimos una función para imprimir el resultado y la interpretación de la velocidad
def imprimir_resultado(velocidad):
    print(f"La velocidad medida es de {velocidad:.2f} km/h.")
    if velocidad > 80:
        print("¡Cuidado! La velocidad es alta. Reduce la velocidad.")
    else:
        print("La velocidad es segura.")

# Definimos la función principal para ejecutar el programa
def main():
    try:
        # Obtener datos del sensor
        velocidad_sensor = obtener_datos_sensor()
        print("Obteniendo datos del sensor...")
        time.sleep(1)

        # Calcular velocidad en función del tiempo y distancia (hipotéticamente proporcionados)
        tiempo_medicion = float(input("Ingrese tiempo de medición:"))  # segundos
        distancia_medicion =  float(input("ingrese distancia de medición:"))   # metros

        velocidad_calculada = calcular_velocidad(tiempo_medicion, distancia_medicion)

        # Obtener el valor absoluto de la velocidad calculada
        velocidad_absoluta_calculada = velocidad_absoluta(velocidad_calculada)

        # Imprimir resultado
        imprimir_resultado(velocidad_absoluta_calculada)

    except ValueError:
        print("Error: Los datos proporcionados por el sensor son inválidos.")
    except ZeroDivisionError:
        print("Error: La distancia no puede ser cero. Revisa los datos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Verificamos si estamos ejecutando este archivo directamente como programa principal
if __name__ == "__main__":
    # Llamamos a la función principal
    main()

