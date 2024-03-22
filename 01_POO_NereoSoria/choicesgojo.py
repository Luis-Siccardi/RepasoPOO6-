import time

def opciongojo(jugador1, jugador2):
    opcion = input("Qué quieres hacer? 1 para atacar Rojo, 2 para atacar Azul, 3 para defender, 4 para usar el Infinito, 5 para usar el púrpura e INFINITO para...: ")
    if opcion == "4":
                if jugador1.tiene_infinito:
                    jugador1.atacar_infinito(jugador2)
                else:
                    print("No has comprado el infinito")
    elif opcion == "5":
                if jugador1.tiene_purpura:
                    jugador1.atacar_purpura(jugador2)
                else:
                    print("No has comprado el Púrpura")
    elif opcion == "INFINITO":
                if jugador1.tiene_expansion:
                    jugador1.atacar_expansion(jugador2)
                else:
                    print("No has comprado la Expansión de Dominio.")
    else:
                if opcion == "1":
                    jugador1.atacar_rojo(jugador2)
                elif opcion == "2":
                    jugador1.atacar_azul(jugador2)
                elif opcion == "3":
                    jugador1.defender()
    time.sleep(1)