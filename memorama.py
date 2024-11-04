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
            return jugador1, jugador2
        elif opcion == 2:
            jugador1 = input("Nombre del Jugador 1: ")
            jugador2 = "Máquina"
            return jugador1, jugador2
        elif opcion == 3:
            jugador1 = "Máquina 1"
            jugador2 = "Máquina 2"
            return jugador1, jugador2
        else:
            print("Error: elige una opción válida (1, 2 o 3).")

def memorama():
    jugador1, jugador2 = menu()

    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-6): "))
        posiciones_tablero = filas * columnas

        if posiciones_tablero < 4 or posiciones_tablero > 30 or posiciones_tablero % 2 != 0:
            print("Error: El número de filas y columnas debe ser par y entre 4 y 30. Inténtalo de nuevo.")
        else:
            break

    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("*")
        tablero.append(fila)
    
    cartas = ["🍎", "🍌", "🍓", "🍇", "🍒", "🍍", "🍉", "🍑", "🍋", "🍈", "🥑", "🥕", "🥦", "🥥", "🥭"]
    pares_cartas = cartas[:(filas * columnas) // 2] * 2
    random.shuffle(pares_cartas)

    tablero_oculto = []
    cont = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(pares_cartas[cont])
            cont += 1
        tablero_oculto.append(fila)

    def mostrar_tablero(tablero):
        for fila in tablero:
            print(" ".join(fila))
        print()
    
    jugador1_puntuacion = 0
    jugador2_puntuacion = 0
    primer_jugador = jugador1

    def jugadorvsjugador(jugador):
        while True:
            fila = int(input(jugador + " elige la fila de la carta: "))
            columna = int(input(jugador + " elige la columna de la carta: "))
            if 1 <= fila < filas and 1 <= columna < columnas:
                return fila, columna
            else:
                print("Esas posiciones de la fila o la columna no se encunetran en el tablero. Inténtalo de nuevo.")
                
    cartas_ocultas = True
    while cartas_ocultas:
        cartas_ocultas = False
        for fila in tablero:
            if "*" in fila:
                cartas_ocultas = True
                break

        print("Turno de " +primer_jugador)
        mostrar_tablero(tablero)
        
    fila1, col1 = jugadorvsjugador(primer_jugador)
    tablero[fila1][col1] = tablero_oculto[fila1][col1]
    mostrar_tablero(tablero)
    fila2, col2 = jugadorvsjugador(primer_jugador)
    tablero[fila2][col2] = tablero_oculto[fila2][col2]
    mostrar_tablero(tablero)
    
    if tablero[fila1][col1] == tablero[fila2][col2]:
        print("¡Par encontrado!")
        if primer_jugador == jugador1:
            jugador1_puntuacion += 1
        else:
            jugador2_puntuacion += 1
    else:
        print("No coincidieron. Se ocultan las cartas.")
        tablero[fila1][col1] = "*"
        tablero[fila2][col2] = "*"
        if primer_jugador == jugador1:
            primer_jugador = jugador2
        else:
            primer_jugador = jugador1

    print("Juego terminado.")
    mostrar_tablero(tablero)
    print("Puntajes finales:")
    print(jugador1 + " : " + jugador1_puntuacion + " puntos")
    print(jugador2 + " : " + jugador2_puntuacion + " puntos")
    if jugador1_puntuacion[jugador1] > jugador2_puntuacion[jugador2]:
        print(jugador1 + " gana el juego")
    elif jugador2_puntuacion[jugador2] > jugador1_puntuacion[jugador1]:
        print(jugador2 + " gana el juego")
    else:
        print("¡Es un empate!")

memorama()


