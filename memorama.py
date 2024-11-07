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
    memoria_maquina = {}

    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-6): "))
        posiciones_tablero = filas * columnas

        if posiciones_tablero < 4 or posiciones_tablero > 30 or posiciones_tablero % 2 != 0:
            print("Error: El número de filas y columnas debe ser par y entre 4 y 30. Inténtalo de nuevo.")
        else:
            break

    tablero = [["*" for _ in range(columnas)] for _ in range(filas)]

    cartas = ["🍎", "🍌", "🍓", "🍇", "🍒", "🍍", "🍉", "🍑", "🍋", "🍈", "🥑", "🥕", "🥦", "🥥", "🥭"]
    pares_cartas = cartas[:posiciones_tablero // 2] * 2
    random.shuffle(pares_cartas)

    tablero_oculto = []
    cont = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(pares_cartas[cont])
            cont += 1
        tablero_oculto.append(fila)

    jugador1_puntuacion = 0
    jugador2_puntuacion = 0
    primer_jugador = jugador1

    asteriscos = True
    while asteriscos:
        print("Turno de " + primer_jugador)
        
        for fila in tablero:
            print(" ".join(fila))
        print()

        if primer_jugador == "Máquina":
            posiciones_disponibles = []
            for i in range(filas):
                for j in range(columnas):
                    if tablero[i][j] == "*":
                        posiciones_disponibles.append((i, j))
            
            par_encontrado = False
            posicion1 = 0
            posicion2 = 0
            for i in range(len(memoria_maquina)):
                for j in range(len(memoria_maquina)):
                    if posicion1 != posicion2:
                        carta1 = memoria_maquina[i]
                        carta2 = memoria_maquina[j]
                        
                        if (posicion1 != posicion2 and
                            carta1 == carta2 and
                            tablero[posicion1][posicion2] == "*" and
                            tablero[posicion1][posicion2] == "*"):
                            
                            fila1 = posicion1
                            columna1 = posicion2
                            par_encontrado = True
                            break
                if par_encontrado:
                    break
            
            if not par_encontrado:
                while True:
                    fila1 = random.randint(0, filas - 1)
                    columna1 = random.randint(0, columnas - 1)
                    if tablero[fila1][columna1] == "*":
                        break
            
            print(primer_jugador, "elige la posición : " ,fila1 + 1, ",", columna1 + 1)
        else:
            while True:
                fila1 = int(input(primer_jugador + " elige la fila de la carta: ")) - 1
                columna1 = int(input(primer_jugador + " elige la columna de la carta: ")) - 1
                if 0 <= fila1 < filas and 0 <= columna1 < columnas and tablero[fila1][columna1] == "*":
                    break
                else:
                    print("Posición inválida o ya descubierta. Inténtalo de nuevo.")

        tablero[fila1][columna1] = tablero_oculto[fila1][columna1]
        if primer_jugador == "Máquina":
            memoria_maquina[(fila2, columna2)] = tablero_oculto[fila2][columna2]
        for fila in tablero:
            print(" ".join(fila))
        print()

        if primer_jugador == "Máquina":
            posiciones_disponibles = []
            for i in range(filas):
                for j in range(columnas):
                    if tablero[i][j] == "*":
                        posiciones_disponibles.append((i, j))
            
            par_encontrado = False
            posicion1 = 0
            posicion2 = 0
            for i in range(len(memoria_maquina)):
                for j in range(len(memoria_maquina)):
                    if posicion1 != posicion2:
                        carta1 = memoria_maquina[i]
                        carta2 = memoria_maquina[j]
                        
                        if (posicion1 != posicion2 and
                            carta1 == carta2 and
                            tablero[posicion1][posicion2] == "*" and
                            tablero[posicion1][posicion2] == "*"):
                            
                            fila2 = posicion1
                            columna2 = posicion2
                            par_encontrado = True
                            break
                if par_encontrado:
                    break
            
            if not par_encontrado:
                while True:
                    fila2 = random.randint(0, filas - 1)
                    columna2 = random.randint(0, columnas - 1)
                    if tablero[fila2][columna2] == "*":
                        break
            
            print(primer_jugador, "elige la posición : " ,fila2 + 1, ",", columna2 + 1)
        else:
            while True:
                fila2 = int(input(primer_jugador + " elige la fila de la carta: ")) - 1
                columna2 = int(input(primer_jugador + " elige la columna de la carta: ")) - 1
                if 0 <= fila2 < filas and 0 <= columna2 < columnas and tablero[fila2][columna2] == "*":
                    break
                else:
                    print("Posición inválida o ya descubierta. Inténtalo de nuevo.")

        tablero[fila2][columna2] = tablero_oculto[fila2][columna2]
        if primer_jugador == "Máquina":
            memoria_maquina[(fila2, columna2)] = tablero_oculto[fila2][columna2]
        for fila in tablero:
            print(" ".join(fila))
        print()

        if tablero[fila1][columna1] == tablero[fila2][columna2]:
            print("¡Par encontrado!")
            if primer_jugador == jugador1:
                jugador1_puntuacion += 2
            else:
                jugador2_puntuacion += 2
        else:
            print("No coincidieron. Se ocultan las cartas.")
            tablero[fila1][columna1] = "*"
            tablero[fila2][columna2] = "*"
            if primer_jugador == jugador1:
                primer_jugador = jugador2
            else:
                primer_jugador = jugador1

        asteriscos = False
        for fila in tablero:
            if "*" in fila:
                asteriscos = True
                break

    print("Juego terminado.")
    for fila in tablero:
        print(" ".join(fila))
    print("Puntaciones finales:")
    print(jugador1, ":", jugador1_puntuacion, "puntos")
    print(jugador2, ":", jugador2_puntuacion, "puntos")
    
    if jugador1_puntuacion > jugador2_puntuacion:
        print(jugador1 + " gana el juego")
    elif jugador2_puntuacion > jugador1_puntuacion:
        print(jugador2 + " gana el juego")
    else:
        print("¡Es un empate!")

memorama()