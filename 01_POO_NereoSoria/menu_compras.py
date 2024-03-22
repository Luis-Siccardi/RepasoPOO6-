def mostrar_menu_compras(jugador):
    while True:
        print("\n¡Bienvenido al menú de compras!")
        print("1. Comprar Ataque Infinito (Costo: 200 monedas)")
        print("2. Comprar Ataque Púrpura (Costo: 700 monedas)")
        print("3. Comprar Expansión de Dominio (Costo: 2000 monedas)")
        print("4. Volver al juego")
        print(f"energía maldita viejo {jugador.monedas}")
        opcion = input("Selecciona una opción: ")
        

        if opcion == "1":
            if jugador.monedas >= 10:
                print("¡Has comprado el Ataque Infinito!")
                jugador.monedas -= 10
                jugador.tiene_infinito = True
            else:
                print("No tienes suficiente energía maldita para comprar el Ataque Infinito.")
        elif opcion == "2":
            if jugador.monedas >= 10:
                print("¡Has comprado el Ataque Púrpura!")
                jugador.monedas -= 10
                jugador.tiene_purpura = True
            else:
                print("No tienes suficiente energía maldita para comprar el Ataque Púrpura.")
        elif opcion == "3":
            if jugador.monedas >= 10:
                print("¡Has comprado la Expansión de Dominio!")
                jugador.monedas -= 10
                jugador.tiene_expansion = True
            else:
                print("No tienes suficiente energía maldita para comprar la Expansión de Dominio.")
        elif opcion == "4":
            return
        else:
            print("todavia no funciona la opcion de volver al juego sorry")