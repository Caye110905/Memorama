def menu():
    print("Bienvenido a Memorama")
    print("Selecciona el modo de juego:")
    print("1. Persona vs Persona")
    print("2. Persona vs Máquina")
    print("3. Máquina vs Máquina")
    print("4. Salir") 
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