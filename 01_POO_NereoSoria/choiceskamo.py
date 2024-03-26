import time

def opcionkamo(jugador1, jugador2):
    opcion = input("Qué quieres hacer? 1 para atacar Golpe, 2 para Lanzar flechas, 3 para defender, 4 para usar el dope, 5 para usar el rayo y 6 para lanzar rafagas: ")
    if opcion == "4":
                if jugador1.tiene_dope:
                    jugador1.atacar_dope()
                else:
                    print("No has comprado el infinito")
    elif opcion == "5":
                if jugador1.tiene_rayo:
                    jugador1.atacar_rayo_sangre(jugador2)
                else:
                    print("No has comprado el Púrpura")
    elif opcion == "6":
                if jugador1.tiene_rafagas_sangre:
                    jugador1.atacar_rafaga(jugador2)
                else:
                    print("No has comprado la Expansión de Dominio.")
    else:
                if opcion == "1":
                    jugador1.atacar_golpe(jugador2)
                elif opcion == "2":
                    jugador1.atacar_flechas_sangre(jugador2)
                elif opcion == "3":
                    jugador1.defender()
    time.sleep(1)