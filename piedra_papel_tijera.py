import random

# Función para obtener la elección de un jugador
def obtener_eleccion(jugador):
    print(jugador, "elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion = input("Ingresa el número de tu elección: ")

    # Validamos que la entrada sea correcta, de lo contrario se elige aleatoriamente
    if opcion not in ["1", "2", "3"]:
        print("Opción no válida. Se elegirá una opción al azar.")
        opcion = str(random.randint(1, 3))

    return int(opcion)

# Función que determina el ganador del juego usando estructuras lógicas
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == 1 and opcion2 == 3) or (opcion1 == 2 and opcion2 == 1) or (opcion1 == 3 and opcion2 == 2):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

# Función principal que maneja el flujo del juego
def jugar():
    print("Juego de Piedra, Papel o Tijera")

    while True:  # Estructura repetitiva para jugar múltiples rondas
        j1 = obtener_eleccion("Jugador 1")
        j2 = obtener_eleccion("Jugador 2")

        print("Jugador 1 eligió:", j1)
        print("Jugador 2 eligió:", j2)

        resultado = determinar_ganador(j1, j2)
        print("Resultado:", resultado)

        # Preguntar si se quiere jugar otra vez
        otra = input("¿Jugar otra vez? (s/n): ")
        if otra.lower() != "s":  # Si la respuesta no es 's', se sale del bucle
            break

    print("Fin del juego.")

# Llamamos a la función para iniciar el juego
jugar()
