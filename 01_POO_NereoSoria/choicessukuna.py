import time

def opcionsukuna(jugador1, jugador2):
    if jugador1.tiene_blackbox:
        ("OPCIONES DE LA BLACKBOX: 7 para lanzar lanza de fuego y 8 para expansion de dominio: ")
    opcion = input("Qué quieres hacer? 1 para atacar Golpe, 2 para atacar Patada, 3 para defender, 4 para esquivar, 5 para usar el corte, 6 para lanzar rafagas de corte, 7 para abrir la blackbox: ")
    if opcion == "5":
                if jugador1.tiene_corte:
                    jugador1.atacar_corte()
                else:
                    print("No has comprado el corte")
    elif opcion == "5":
                if jugador1.tiene_rafagas_corte:
                    jugador1.atacar_rafagas_corte(jugador2)
                else:
                    print("No has comprado el ráfaga")
    elif opcion == "6":
                if jugador1.tiene_blackbox:
                    jugador1.atacar_blackbox(jugador2)
                else:
                    print("No has comprado la BlackBox.")
    elif opcion == "8":
                if jugador1.tiene_lanza_fuego:
                       jugador1.atacar_lanza_fuego(jugador2)
                else:
                       print("No has comprado la lanza de fuego")
    elif opcion == "9":
                if jugador1.tiene_expansion:
                       jugador1.atacar_expansion(jugador2)
                else:
                       print("No tienes la expansion de dominio")
    else:
                if opcion == "1":
                    jugador1.atacar_golpe(jugador2)
                elif opcion == "2":
                    jugador1.atacar_patada(jugador2)
                elif opcion == "3":
                    jugador1.defender()
                
                elif opcion == "4":
                      jugador1.atacar_esquivar()
                
    time.sleep(1)