import random

def menu():
    print("Bienvenido a Memorama")
    print("Selecciona el modo de juego:")
    print("1. Persona vs Persona")
    print("2. Persona vs Máquina")
    print("3. Máquina vs Máquina")
    while True:
        opcion = int(input("Elige una opción (1-3): "))
        if opcion == 1:
            jugador1 = input("Nombre del Jugador 1: ")
            jugador2 = input("Nombre del Jugador 2: ")
            break
        elif opcion == 2:
            jugador1 = input("Nombre del Jugador 1: ")
            jugador2 = "Máquina"
            break
        elif opcion == 3:
            jugador1 = "Máquina 1"
            jugador2 = "Máquina 2"
            break
        else:
            print("Error: elige una opción válida (1, 2 o 3).")

menu()

def tablero():
    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-6): "))
        posiciones_tablero = filas * columnas

        if posiciones_tablero < 4 or posiciones_tablero > 30 or posiciones_tablero % 2 != 0:
            print("Error: El número de filas y columnas debe ser par y entre 4 y 30. Intentalo de nuevo.")
        else:
            break

    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("*")
        tablero.append(fila)

    print("Tablero creado con las cartas boca abajo: ")
    for fila in tablero:
        print(" ".join(fila))
    print()

    cartas = ["🍎", "🍌", "🍓", "🍇", "🍒", "🍍", "🍉", "🍑", "🍋", "🍈", "🥑", "🥕", "🥦", "🥥", "🥭"]
    
    pares_cartas = (cartas * 2)[:posiciones_tablero]
    random.shuffle(pares_cartas)

    tablero_oculto = []
    cont = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(pares_cartas[cont])
            cont += 1
        tablero_oculto.append(fila)

    print("Tablero creado con las cartas visibles: ")
    for fila in tablero_oculto:
        print(" ".join(fila))
    print()

tablero()

